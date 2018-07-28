#!/usr/bin/env python
from distutils.core import setup


setup(name='havok-spider',
        version='0.1',
        description='Web site testing tool',
        author='Kirt Saelensminde',
        author_email='kirit@felspar.com',
        url='https://kirit.com/havok-spider',
        scripts=['bin/havok-spider'],
        install_requires=['beautifulsoup4'],
        packages=['havok'],
    )
