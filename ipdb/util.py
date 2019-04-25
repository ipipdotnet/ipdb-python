# -*- coding: utf-8 -*-
"""
    :copyright: ©2018 by IPIP.net
"""

import gzip
import sys


def bytes2long(a, b, c, d):
    return convert(a) << 24 | convert(b) << 16 | convert(c) << 8 | convert(d)


def convert(v):
    if v == "" or v == 0:
        return 0
    if sys.version_info.major >= 3:
        return v
    else:
        return ord(v)


def read_file(path, compression=None):
    if compression is None:
        return _read_file_default(path)
    elif compression == 'gzip':
        return _read_file_gzip(path)
    raise Exception('unsupported compression type: {}'.format(compression))


def _read_file_default(path):
    with open(path, "rb") as f:
        content = f.read()
    return content


def _read_file_gzip(path):
    with gzip.open(path, "rb") as f:
        content = f.read()
    return content
