#! /usr/bin/env python

"""Executes OAK

Commands:
placeholder
"""

from arandomness.argparse import CopyRight
import argparse
from pkg_resources import resource_string
import sys

__author__ = 'Alex Hyer'
__email__ = 'theonehyer@gmail.com'
__license__ = 'GPLv3'
__maintainer__ = 'Alex Hyer'
__status__ = 'Planning'
__version__ = resource_string(__name__, '../VERSION').decode('ascii')

# Obtain and store all copyright data
copyRight = """
Copyright:
    __main__.py  Executes OAK
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

gplV3 = resource_string(__name__, '../../LICENSE').decode('ascii')


def main(arguments=None):
    """OAK's main entry point: controls program flow

    Args:
        arguments (list): list of string to optionally pass to argparse
    """
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.
                                     RawDescriptionHelpFormatter)
    parser.add_argument('--copyright',
                        action=CopyRight,
                        copyright_text=copyRight)
    parser.add_argument('--copyright-full',
                        action=CopyRight,
                        copyright_text=gplV3)
    parser.add_argument('--version',
                        action='version',
                        version=__version__)
    if arguments is None:
        args = parser.parse_args()  # Parse from sys.argv
    else:
        args = parser.parse_args(args=arguments)  # Parse from arguments list


if __name__ == '__main__':
    main()
    sys.exit(0)
