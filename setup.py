#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

# import CI_sample

setup(
    name='ci',
    # version=CI_sample.__version__,
    description='Infortrend Cloud Storage Centralize Command Line',

    author='Infortrend',
    url='http://www.infortrend.com',
    author_email='tsd@infortrend.com',

    platforms='any',

    packages=find_packages(exclude=['tests']),

    entry_points={
        'console_scripts': [
            'CI_sample = CI_sample.CI_sample:cisample'
        ]
    },

    # data_files=[('clics', ['clics/version.json'])],

    test_suite='nose.collector',

    install_requires=[
        'xmltodict>=0.9.2',
        'future>=0.15.2',
        'pykka>=1.2.1',
    ],

    setup_requires=[
        'flake8>=2.4.1',
        'nose>=1.3.7',
    ],

    tests_require=[
        'coverage>=4.0',
        'mock>=1.3.0',
    ],
)
