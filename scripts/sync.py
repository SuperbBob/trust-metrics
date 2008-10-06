#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
this script syncronize local datasets database with the remote database (on trustlet.org).
It uses svn.

First of all it'll download missed datasets.
Then merge them with the local version of them.
Finally changes will be committed.

main directory dataset: ~/datasets
svn hidden directory: ~/.datasets

Parameters:
   --no-update: no svn update. ¡¡¡ Dangerous option !!!
   --no-upload: no upload generated files
'''

import os
import sys
import shutil

from trustlet.helpers import merge_cache,mkpath

HOME = os.environ['HOME']
HIDDENPATH = os.path.join(HOME,'.datasets')
DATASETSPATH = os.path.join(HOME,'datasets')
CURDIR = os.getcwd()
SVNCO = 'svn co --non-interactive http://www.trustlet.org/trustlet_dataset_svn %s' % HIDDENPATH
SVNUP = 'svn up --username anybody --password a'
SVNCI = 'svn ci --username anybody --password a -m="auomatic commit (sync.py)"'
SVNADD = 'svn add %s'

def main():

    if 'help' in sys.argv:
        print __doc__
        return

    if not os.path.isdir(HIDDENPATH) or not os.path.isdir(os.path.join(HIDDENPATH,'.svn')):
        os.chdir(HOME)
        os.system(SVNCO)
    elif not '--no-update' in sys.argv:
        os.chdir(HIDDENPATH)
        os.system(SVNUP)

    merge(HIDDENPATH,DATASETSPATH,not '--no-upload' in sys.argv)

    os.chdir(CURDIR)

def diff(f,g):
    '''
    return True if 2 file are equals
    '''
    if type(f) is str:
        f = file(f)
    if type(g) is str:
        g = file(g)

    while True:
        bf = f.read(512)
        bg = g.read(512)
        
        if bf != bg:
            f.close()
            g.close()
            return False
        if not bf:
            f.close()
            g.close()
            return True

def merge(svn,datasets,upload=True):
    added = updated = merged = 0
    updatedc2 = set()
    # from svn to datasets
    for dirpath,dirnames,filenames in os.walk(svn):
        if '.svn' in dirpath:
            continue
        destbasepath = dirpath.replace(svn,datasets)
        
        print destbasepath
        print dirpath
        print dirnames
        print filenames
        print

        for f in filenames:
            assert os.path.isfile(f)
        for d in dirnames:
            assert os.path.isdir(d)

        if not os.path.isdir(destbasepath):
            os.mkdir(destbasepath)

        for filename in filenames:
            srcpath = os.path.join(dirpath,filename)
            dstpath = os.path.join(destbasepath,filename)
            
            if os.path.isfile(dstpath):
                if not diff(srcpath,dstpath):
                    # file modified
                    if filename.endswith('.c2'):
                        print 'merging file %s with new version' % filename
                        updatedc2.add(dstpath)
                        merged += 1
                        # priority: dstpath
                        merge_cache(srcpath,dstpath)
                    else:
                        #update
                        print 'updating file',filename
                        updated += 1
                        shutil.copy(srcpath,dstpath)
            else:
                #adding
                print 'adding file',filename
                added += 1
                shutil.copy(srcpath,dstpath)


    if added:
        print '# of added files:',added
    if updated:
        print '# of updated files:',updated
    if merged:
        print '# of merged files:',merged
    
    # from datasets to svn
    if upload:
        print 'Upload on server'
        added = 0

        # to adding files
        os.chdir(svn)

        #copy *new* files and updated c2 to upload dir (svn)
        for dirpath,dirnames,filenames in os.walk(datasets):
            destbasepath = dirpath.replace(datasets,svn)

            for filename in filenames:
                srcpath = os.path.join(dirpath,filename)
                dstpath = os.path.join(destbasepath,filename)
            
                if not os.path.isfile(dstpath):
                    print 'adding file',filename
                    added += 1
                    mkpath(dstpath, lambda x: __import__('pprint').pprint(x))
                    shutil.copy(srcpath,dstpath)
                    os.system(SVNADD % dstpath)
                elif srcpath in updatedc2:
                    print 'merging file',filename
                    shutil.copy(srcpath,dstpath)

        os.system(SVNCI)

        if added:
            print '# of added files to server repository:',added
        

if __name__=="__main__":
    main()
