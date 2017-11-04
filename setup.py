#! /usr/bin/env python

"""Setup file to build and install oak

Copyright:

    setup.py build and install oak
    Copyright (C) 2017  Alex Hyer

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from pkg_resources import resource_string
from setuptools import setup

__author__ = 'Alex Hyer'
__email__ = 'theonehyer@gmail.com'
__license__ = 'GPLv3'
__maintainer__ = 'Alex Hyer'
__status__ = 'Alpha'
__version__ = resource_string(__name__, '../VERSION').decode('ascii')

setup(name='oak',
      version=__version__,
      description='Ontological Annotation using Kegg',
      classifiers=[
          'Development Status :: 1 - Pre-production',  # Edit this?
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Natural Language :: English',
          'Operating System :: OS Independent',  # Maybe?
          'Programming Language :: Python :: 3.5',
          'Topic :: Scientific/Engineering :: Bio-Informatics'
      ],
      keywords='oak ontological annotation bioinformatics',
      url='https://github.com/TheOneHyer/aspgen',
      download_url='https://github.com/Brazelton-Lab/oak/tarball/'
                   '{0}'.format(__version__),
      author='Alex Hyer',
      author_email='theonehyer@gmail.com',
      license='GPLv3',
      packages=[
          'oak',
          'oak.bin',
          'oak.lib'
      ],
      include_package_data=True,
      entry_points={
          'console_scripts': [
              'oak = oak.bin.__main__:main'
          ]
      },
      requires=[
          'arandomness'
      ]
      )
