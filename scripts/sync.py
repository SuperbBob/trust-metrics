#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
this script syncronizes local datasets database with the remote database (on trustlet.org).
It uses svn.

First of all it'll download missed datasets.
Then merge them with the local version of them.
 - Only c2 file are mergerd. If a regular file yet exists on client it won't updated.
Finally *all* changes will be committed.
 - Backup files (ends with ~) will not uploaded.
 - Files and directory that begin with _ will not uploaded too.

main directory dataset: <basepath>/datasets
svn hidden directory: <basepath>/.datasets

sync creates ~/datasets and ~/.datasets links

sync.py [basepath] [other options]
  or
sync rm path [other options]

 - path can be a dir or a file

Options:
   --no-update: no svn update. ¡¡¡ Dangerous option !!!
   --no-upload: no upload generated files
   --verbose | -v
'''

import os
import os.path as path
import sys
import shutil
import re
import time

from trustlet.helpers import merge_cache,mkpath,md5file

HOME = os.environ['HOME']
CURDIR = os.getcwd()
SVNCO = 'svn co --non-interactive http://www.trustlet.org/trustlet_dataset_svn "%s"'
SVNUP = 'svn up --username anybody --password a'
SVNCI = 'svn ci --username anybody --password a -m "auomatic commit (sync.py)"'
SVNADD = 'svn add "%s"'

CONFLICT =  '''You might added files yet stored on svn.
You can execute:
cd ~/.datasets
svn revert `file(s) added`
mv or rm `file(s) added`
sync.py
Now you can readd your file with sync.py
'''

def svnadd(p):
    assert not os.system(SVNADD % p)

def svnaddpath(p):
    
    assert path.abspath(p)!='/',p

    if path.isdir(path.join(p,'.svn')):
        return True
    
    if svnaddpath(path.join(p,os.pardir)):
        svnadd(p)

    return False

def main():

    if 'help' in sys.argv or '--help' in sys.argv:
        print __doc__
        return

    if sys.argv[1:] and sys.argv[1][0]!='-':
        basepath = path.realpath(sys.argv[1])
    else:
        basepath = HOME

    hiddenpath = path.join(basepath,'.datasets')
    datasetspath = path.join(basepath,'datasets')

    #remove old links
    if path.islink(path.join(HOME,'.datasets')):
        os.remove(path.join(HOME,'.datasets'))
    if path.islink(path.join(HOME,'datasets')):
        os.remove(path.join(HOME,'datasets'))

    if basepath != HOME:
        path1 = path.join(HOME,'.datasets')
        path2 = path.join(HOME,'datasets')
        assert not path.islink(path1) and not path.exists(path1),'remove '+path1
        assert not path.islink(path2) and not path.exists(path2),'remove '+path2
        assert not os.system('ln -s "%s" "%s"' % (hiddenpath,path1))
        assert not os.system('ln -s "%s" "%s"' % (datasetspath,path2))

    sys.argv = set(sys.argv)

    if '--verbose' in sys.argv:
        sys.argv.append('-v')
    
    #files removed from svn
    to_remove = []

    tstampup = 0
    if not path.isdir(hiddenpath) or not path.isdir(path.join(hiddenpath,'.svn')):
        os.chdir(HOME)
        shutil.rmtree(hiddenpath)
        assert not os.system(SVNCO % hiddenpath)
    elif not '--no-update' in sys.argv:
        os.chdir(hiddenpath)
        
        #add all svn dir files to to_remove
        for dirpath,dirs,files in os.walk(hiddenpath):
            if not '.svn' in dirpath:
                # foreach file saves relative path
                to_remove += [path.join(dirpath,x) for x in files]

        #timestamp update
        tstampup = int(time.time())
        assert not os.system(SVNUP),'Update failied. '+CONFLICT

        to_remove = set(to_remove)
        for dirpath,dirs,files in os.walk(hiddenpath):
            if not '.svn' in dirpath:
                # remove from to_remove files yet in datasets dir only if
                # they have not been modified.
                to_remove.difference_update(set([path.join(dirpath,x) for x in files
                                                 if mtime(path.join(dirpath,x))<tstampup]))

        #print to_remove
        for f in to_remove:
            f = f.replace(hiddenpath,datasetspath)
            if path.isfile(f):
                print "I'm removing",f
                os.remove(f)
    
    merge(hiddenpath,datasetspath,not '--no-upload' in sys.argv)

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

mtime = lambda f: int(os.stat(f).st_mtime)

def merge(svn,datasets,upload=True):
    '''
    to_remove: files removed from svn (svn directory paths)
    '''
    added = updated = merged = 0
    updatedc2 = set()
    updatedfiles = set()

    re_svnconflict = re.compile('.*\.r\d+$') #ends with .r[num]

    # from svn to datasets
    for dirpath,dirnames,filenames in os.walk(svn):
        if '.svn' in dirpath:
            continue

        # Seems that in dirnames there are some filenames and viceversa.
        test = (dirnames,filenames)
        names = dirnames + filenames
        dirnames = [x for x in names if path.isdir(path.join(dirpath,x))]
        filenames = [x for x in names if path.isfile(path.join(dirpath,x))]
        assert (dirnames,filenames)==test,'Seems that in dirnames there are some filenames and viceversa.'
        #

        destbasepath = dirpath.replace(svn,datasets)
        
        if '-v' in sys.argv:
            print destbasepath
        if not path.isdir(destbasepath):
            assert not path.isfile(destbasepath),destbasepath
            os.mkdir(destbasepath)

        for filename in filenames:
            #print filename
            srcpath = path.join(dirpath,filename)
            dstpath = path.join(destbasepath,filename)
            
            if path.isfile(dstpath):
                if not diff(srcpath,dstpath):
                    # file modified
                    if filename.endswith('.c2'):
                        print 'merging file %s with new version' % filename
                        updatedc2.add(dstpath)
                        merged += 1
                        # priority: dstpath
                        merge_cache(srcpath,dstpath)
                    else:
                        print 'file %s differs from client to server. The client version will be kept.' % filename
                        updatedfiles.add(dstpath)
            elif filename[0]!='_' and not re.match(re_svnconflict,filename) and not filename.endswith('.mine'):
                #adding
                print 'adding file',filename
                added += 1
                #print srcpath,dstpath
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

            if path.sep+'_' in dirpath:
                # not upload dirs _*
                print 'Directory %s will not uploaded' % path.split(dirpath)[1]
                continue

            for filename in filenames:
                if filename.endswith('~'):
                    # skip backup files
                    continue
                if filename.startswith('_') or re.match(re_svnconflict,filename) or filename.endswith('.mine'):
                    # not upload files _*
                    print 'File %s will not uploaded' % filename
                    continue

                srcpath = path.join(dirpath,filename)
                dstpath = path.join(destbasepath,filename)
            
                if not path.isfile(dstpath):
                    print 'adding file',filename
                    added += 1

                    mkpath(destbasepath)
                    svnaddpath(destbasepath)
                    shutil.copy(srcpath,destbasepath)
                    svnadd(dstpath)
                elif srcpath in updatedc2:
                    print 'merging file',filename
                    shutil.copy(srcpath,dstpath)
                elif srcpath in updatedfiles:
                    print 'updating file',filename
                    shutil.copy(srcpath,dstpath)

        assert not os.system(SVNCI),CONFLICT

        if added:
            print '# of added files to server repository:',added
        

if __name__=="__main__":
    main()
