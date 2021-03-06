#!/usr/bin/env python

from focusyn import __version__
PROJ_METADATA = 'meta.json'

import os, json
here = os.path.abspath(os.path.dirname(__file__))
proj_info = json.loads(open(os.path.join(here, PROJ_METADATA)).read())
README = open(os.path.join(here, 'README.md')).read()
CHANGELOG = open(os.path.join(here, 'CHANGELOG.rst')).read()

# This creates a symbolic link to our distractions file
distractions = os.path.join(here, 'distractions')
os.symlink(distractions, '/etc/distractions')

from setuptools import setup, find_packages
setup(
    name = proj_info['name'],
    version = __version__,

    author = proj_info['author'],
    author_email = proj_info['author_email'],
    # url = proj_info['url'],
    license = proj_info['license'],

    description = proj_info['description'],
    keywords = proj_info['keywords'],

    long_description = README + '\n\n' + CHANGELOG,

    packages = find_packages(),

    platforms = 'any',
    zip_safe = False,
    include_package_data = True,

    classifiers = proj_info['classifiers'],

    entry_points = {'console_scripts': proj_info['console_scripts']}
)
