#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import, print_function

import io
from os.path import dirname, join

from setuptools import setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


setup(
    name='tox-sitepackages-example',
    license='BSD-2-Clause',
    description='An example package. Generated with cookiecutter-pylibrary.',
    long_description='An example package.',
    version='0.0.0',
    author='David A. Hannasch',
    author_email='David.A.Hannasch@gmail.com',
    url='https://github.com/dHannasch/tox-sitepackages-example',
    packages=[],
    py_modules=[],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Utilities',
    ],
    project_urls={
        'Documentation': 'https://tox-sitepackages-example.readthedocs.io/',
    },
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    install_requires=[
        'click',
        'detectron2',
        # eg: 'aspectlib==1.1.1', 'six>=1.7',
    ],
)
