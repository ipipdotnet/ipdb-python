# -*- coding: utf-8 -*-
"""
    :copyright: ©2018 by IPIP.net
"""


class DatabaseError(Exception):
    pass


class NoSupportLanguageError(Exception):
    pass


class NoSupportIPv6Error(Exception):
    pass


class NoSupportIPv4Error(Exception):
    pass