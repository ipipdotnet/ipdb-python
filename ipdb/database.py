# -*- coding: utf-8 -*-
"""
    :copyright: ©2018 by IPIP.net
"""

import ipaddress
import json
import sys

from .util import bytes2long
from .exceptions import NoSupportIPv4Error, NoSupportIPv6Error, NoSupportLanguageError, DatabaseError, IPNotFound


class MetaData(object):
    def __init__(self, **kwargs):
        self.fields = kwargs['fields']
        self.node_count = kwargs['node_count']
        self.total_size = kwargs['total_size']
        self.build = kwargs['build']
        self.languages = kwargs['languages']
        self.ip_version = kwargs['ip_version']


class Reader:

    _meta = {}
    data = b""

    _v4offset = 0
    _v6offsetCache = {}

    def __init__(self, name):
        self._v4offset = 0
        self._v6offsetCache = {}

        file = open(name, "rb")
        self.data = file.read()
        self._file_size = len(self.data)
        file.close()
        meta_length = bytes2long(self.data[0], self.data[1], self.data[2], self.data[3])
        if sys.version_info < (3,0):
            meta = json.loads(str(self.data[4:meta_length + 4]))
        else:
            meta = json.loads(str(self.data[4:meta_length + 4], 'utf-8'))

        self._meta = MetaData(**meta)
        if len(self._meta.languages) == 0 or len(self._meta.fields) == 0:
            raise DatabaseError("database meta error")
        if self._file_size != (4 + meta_length + self._meta.total_size):
            raise DatabaseError("database size error")

        self.data = self.data[4+meta_length:]

    def _read_node(self, node, idx):
        off = idx * 4 + node * 8
        return bytes2long(self.data[off], self.data[off + 1], self.data[off + 2], self.data[off + 3])

    def _find_node(self, ip):

        if ip.version == 6:
            bit_count = 128
        else:
            bit_count = 32

        idx = 0
        node = 0
        key = ip.packed[0:2]
        if bit_count == 32:
            if self._v4offset == 0:
                i = 0
                while i < 96:
                    if i >= 80:
                        node = self._read_node(node, 1)
                    else:
                        node = self._read_node(node, 0)
                    i += 1
                self._v4offset = node
            else:
                node = self._v4offset
        else:
            val = self._v6offsetCache.get(key, -1)
            if val > -1:
                idx = 16
                node = val

        packed = bytearray(ip.packed)
        while idx < bit_count:
            if node > self._meta.node_count:
                break
            node = self._read_node(node, (1 & (packed[idx >> 3] >> 7 - (idx % 8))))
            idx += 1
            if idx == 16 and bit_count == 128:
                self._v6offsetCache[key] = node

        if node > self._meta.node_count:
            return node
        raise IPNotFound("ip not found")

    def _resolve(self, node):
        resolved = node - self._meta.node_count + self._meta.node_count * 8
        size = bytes2long(0, 0, self.data[resolved], self.data[resolved + 1])
        if (resolved+2+size) > len(self.data):
            raise DatabaseError("database is error")
        return self.data[resolved+2:resolved+2+size]

    def find(self, addr, language):
        off = self._meta.languages.get(language)
        if off is None:
            raise NoSupportLanguageError(language + " is not support")

        ipv = ipaddress.ip_address(addr)
        if ipv.version == 6:
            if self.is_support_ipv6() is False:
                raise NoSupportIPv6Error("database is not support ipv6")
        elif ipv.version == 4:
            if self.is_support_ipv4() is False:
                raise NoSupportIPv4Error("database is not support ipv4")

        node = self._find_node(ipv)
        if node is None:
            return None

        bs = self._resolve(node)
        if bs is None:
            return None

        tmp = bs.decode("utf-8").split("\t")
        end = off + len(self._meta.fields)
        if len(tmp) < end:
            raise DatabaseError("database is error")

        return tmp[off:off+len(self._meta.fields)]

    def find_map(self, addr, language):
        loc = self.find(addr, language)
        if loc is None:
            return None
        m = {}
        for idx, value in enumerate(self._meta.fields):
            m[value] = loc[idx]
        return m


    def get_meta_data(self):
        return self._meta

    def support_languages(self):
        ls = []
        for p in self._meta.languages:
            ls.append(p)
        return ls

    def support_fields(self):
        return self._meta.fields

    def is_support_ipv4(self):
        return (self._meta.ip_version & 0x01) == 0x01

    def is_support_ipv6(self):
        return (self._meta.ip_version & 0x02) == 0x02

    def build_utc_time(self):
        return self._meta.build
