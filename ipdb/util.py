# -*- coding: utf-8 -*-
"""
    :copyright: ©2018 by IPIP.net
"""


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
