#!/usr/bin/env python

import os
from setuptools import setup

setup(
    name='reddit',
    version='1.0',
    description='View reddit\'s RSS feed from your terminal.',
    author='jmau5',
    author_email='its.jmau5@gmail.com',
    url='http://github.com/jmau5/reddit.py',
    install_requires=[
        'feedparser',
    ],
)

os.system('rm -r build/ dist/ reddit.egg-info/')

move_givemode = raw_input('Copy reddit.py to /usr/local/bin and give mode +x (y/n)? ')

if move_givemode == 'y':
    os.system('sudo chmod +x reddit.py')
    os.system('sudo cp reddit.py /usr/local/bin/reddit')
