#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name='file-json-logger',
    version='0.1.3',
    packages=find_packages(),
    requires=['python (>= 2.5)'],
    description='It allows you save json-logs into file. Special for Kibana',
    long_description=readme,
    author='Stepan Filatov',
    author_email='stepa-filatov@yandex.ru',
    url='https://github.com/sfilatov96/file-json-logger',
    download_url='https://github.com/sfilatov96/file-json-logger/tarball/master',
    license='MIT License',
    keywords=['json-logger', "file-json-logger", ""],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
    ],
)
