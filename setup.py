#!/usr/bin/env python

# ----------------------------------------------------------------------------
# Copyright (c) 2016--, canvas development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

import re
import ast

from setuptools import find_packages, setup


classes = """
    Development Status :: 0 - pre-alpha
    License :: OSI Approved :: BSD License
    Topic :: Software Development :: Libraries
    Topic :: Scientific/Engineering
    Topic :: Scientific/Engineering :: Bio-Informatics
    Programming Language :: Python :: 2
    Programming Language :: Python :: 2 :: Only
    Operating System :: Unix
    Operating System :: POSIX
    Operating System :: MacOS :: MacOS X
"""
classifiers = [s.strip() for s in classes.split('\n') if s]

description = ('Compositional data analysis tools and visualizations')

with open('README.md') as f:
    long_description = f.read()


# version parsing from __init__ pulled from Flask's setup.py
# https://github.com/mitsuhiko/flask/blob/master/setup.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('canvas/__init__.py', 'rb') as f:
    hit = _version_re.search(f.read().decode('utf-8')).group(1)
    version = str(ast.literal_eval(hit))

setup(name='canvas',
      version=version,
      license='BSD',
      description=description,
      long_description=long_description,
      author="canvas development team",
      author_email="jamietmorton@gmail.com",
      maintainer="canvas development team",
      maintainer_email="jamietmorton@gmail.com",
      packages=find_packages(),
      setup_requires=['numpy >= 1.9.2'],
      install_requires=[
          'IPython >= 3.2.0',
          'matplotlib >= 1.4.3',
          'numpy >= 1.9.2',
          'pandas >= 0.18.0',
          'scipy >= 0.15.1',
          'nose >= 1.3.7',
          'scikit-bio == 0.4.2',
          'ete3',
          'biom-format'
      ],
      classifiers=classifiers,
      package_data={
          }
      )
