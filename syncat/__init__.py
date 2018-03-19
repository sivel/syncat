#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2017 Matt Martz
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from __future__ import print_function

import argparse
import sys
import textwrap

from pygments import highlight
from pygments.formatters import Terminal256Formatter as Formatter
from pygments.lexers import guess_lexer, get_lexer_by_name, get_all_lexers
from pygments.styles import get_all_styles, get_style_by_name
from pygments.util import ClassNotFound

from .solarized256 import Solarized256Style


__version__ = '1.0.1'


class _HelpFormatter(argparse.HelpFormatter):
    def _split_lines(self, text, width):
        if '\n' in text:
            return text.splitlines()
        return textwrap.wrap(text, width)


def parse_args():
    show_lexers = '--lexer-help' in sys.argv
    parser = argparse.ArgumentParser(
        prog='syncat',
        formatter_class=_HelpFormatter
    )
    parser.add_argument(
        'file',
        type=argparse.FileType('r'),
        default='-',
        nargs='?',
        help='File to print with syntax highlighting. Defaults to stdin'
    )
    parser.add_argument(
        '--force-color',
        action='store_true',
        help='Force color output, even when stdout is not a TTY'
    )

    all_styles = sorted(list(get_all_styles()) + ['solarized256'])
    parser.add_argument(
        '--style',
        type=str,
        choices=all_styles,
        default='solarized256',
        metavar='STYLE',
        help='Syntax highlighting style. Choices:\n%s' % '\n'.join(all_styles)
    )
    parser.add_argument(
        '--lexer-help',
        action='help',
        help='List help and options for the --lexer argument'
    )

    all_lexers = sorted(get_all_lexers(), key=lambda l: l[1])
    all_lexer_aliases = [alias for lexer in all_lexers for alias in lexer[1]]
    lexers = parser.add_mutually_exclusive_group()
    lexers.add_argument(
        '--lexer',
        type=str,
        dest='lexer',
        choices=all_lexer_aliases,
        help='Lexer to use for syntax highlighting. Defaults to guessing '
             'based on the file contents. Use --lexer-help for a list of '
             'all lexers. Can be used in the form of --lexer LEXER or as '
             '--LEXER such as --lexer json or --json',
        metavar='LEXER'
    )
    for name, aliases, _, _ in all_lexers:
        lexers.add_argument(
            *('--%s' % a for a in aliases),
            dest='lexer',
            action='store_const',
            const=aliases[0],
            help=argparse.SUPPRESS if not show_lexers else name
        )

    return parser.parse_args()


def main():
    args = parse_args()
    try:
        text = args.file.read()
    except Exception as e:
        raise SystemExit(e)
    try:
        try:
            style = get_style_by_name(args.style)
        except ClassNotFound:
            style = Solarized256Style

        try:
            lexer = get_lexer_by_name(args.lexer)
        except ClassNotFound:
            lexer = guess_lexer(text)

        if sys.stdout.isatty() or args.force_color:
            print(
                highlight(
                    text,
                    lexer,
                    Formatter(
                        style=style
                    ),
                ),
                end=''
            )
        else:
            print(text, end='')
    except IOError:
        pass


if __name__ == '__main__':
    main()
