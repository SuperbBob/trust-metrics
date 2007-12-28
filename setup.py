#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup script for networkx

"""

from glob import glob
import os
import sys
if os.path.exists('MANIFEST'):
    os.remove('MANIFEST')

from distutils.core import setup
import trustlet

version = trustlet.__version__

if sys.argv[-1] == 'setup.py':
    print "To install, run 'python setup.py install'"
    print

if sys.version_info[:2] < (2, 3):
    print "trustlet requires Python version 2.3 or later (%d.%d detected)." % \
          sys.version_info[:2]
    sys.exit(-1)


docdirbase  = 'share/doc/trustlet-%s' % version
data = [# (docdirbase, glob("doc/*.txt")),
        (os.path.join(docdirbase, 'examples'),glob("examples/*.py")),
        # (os.path.join(docdirbase, 'examples'),glob("doc/examples/*.dat")),
        # (os.path.join(docdirbase, 'examples'),glob("doc/examples/*.edges")),
        # (os.path.join(docdirbase, 'data'),glob("doc/data/*ls")),
        ]

package_data     = {'': ['*.txt'],} 


setup(	name = 'trustlet',
	version = version,
	description = 'Analyse trust metrics on social networks',
	author = 'Kasper Souren, Paolo Massa and others',
	author_email = 'kasper.souren@gmail.com',
	url = 'http://trustlet.org/wiki/Code',
	license = 'GPL',
	platforms = ["any"],
        # see http://www.python.org/pypi?%3Aaction=list_classifiers
	classifiers = ['Development Status :: 2 - Pre-Alpha',
                       'Intended Audience :: Science/Research', 
                       'License :: OSI Approved :: GNU General Public License (GPL)', 
                       'Natural Language :: English',			
                       'Operating System :: OS Independent',		
                       'Programming Language :: Python',		
                       'Topic :: Scientific/Engineering :: Visualization',
                       'Topic :: Software Development :: Libraries :: Python Modules'
                       ],
	long_description = "\n".join(trustlet.__doc__.split('\n')),
	# py_modules = ['trustlet', 'pymmetry'],
        scripts = ['scripts/dataset-downloader'],
        packages = ['trustlet', 'trustlet.pymmetry', 'trustlet.Dataset'],
        data_files = data,
        package_data = package_data,

        # this doesn't work really well with Python 2.5.1 and
        # setuptools 0.6c6 on guaka's RH machine called power at IRST
        install_requires = ['igraph',
                            'pygraphviz',
                            'pyparsing',
                            'networkx',
                            'numpy',
                            'scipy',
                            ]  
        )