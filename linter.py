#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Jan T. Sott
# Copyright (c) 2017 Jan T. Sott
#
# https://github.com/idleberg/SublimeLinter-contrib-iscc
#
# License: MIT
#

"""This module exports the Iscc plugin class."""

from SublimeLinter.lint import Linter, util


class Iscc(Linter):

    """Provides an interface to the ISCC executable."""

    cmd = ('ISCC.exe', '/Q', '/O-', '@')
    defaults = {
        'selector': 'source.inno'
    }
    regex = (
        r'^Error on line (?P<line>\d+) in (?P<file>.*\.iss): (?P<message>.+)$'
    )
    multiline = True
    error_stream = util.STREAM_STDERR
    line_col_base = (1, 1)
