#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from distutils.util import convert_path

module_name = 'pascua'

with open('README.md') as f:
    long_description = f.read()

with open(convert_path('{}/_version.py'.format(module_name))) as file:
    main_ns = dict()
    exec(file.read(), main_ns)
    module_version = main_ns['__version__']

setup(
    name=module_name,
    version=module_version,
    url='https://github.com/garciparedes/pascua',
    author='Sergio García Prado',
    author_email='sergio@garciparedes.me',
    description='Python library to perform code execution in fully isolated environments',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[

    ],
)
