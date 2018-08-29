# -*- coding: utf-8 -*-
"""
    :copyright: ©2018 by IPIP.net
"""

import ipaddress
import json
from .meta import MetaData
from .info import IPInfo
from .util import bytes2long


class Reader:

    meta = {}
    data = b""

    file = False
    file_size = 0

    v4offset = 0
    v6offsetCache = {}

    def __init__(self, name):
        self.file = open(name, "rb")
        self.data = self.file.read()
        self.file_size = len(self.data)

        meta_length = bytes2long(self.data[0], self.data[1], self.data[2], self.data[3])
        meta = json.loads(self.data[4:meta_length+4])

        self.meta = MetaData(**meta)
        self.data = self.data[4+meta_length:]

    def _find_node(self, ip):

        if ip.version == 6:
            bit_count = 128
        else:
            bit_count = 32

        i = 0
        node = 0
        key = ip.packed[0:2]
        if bit_count == 32:
            if self.v4offset == 0:
                i = 0
                while i < 96:
                    if i >= 80:
                        node = self.read_node(node, 1)
                    else:
                        node = self.read_node(node, 0)
                    i += 1
                self.v4offset = node
            else:
                node = self.v4offset
        else:
            val = self.v6offsetCache.get(key, -1)
            if val > -1:
                i = 16
                node = val

        while i < bit_count:
            if node > self.meta.node_count:
                break
            node = self.read_node(node, (1 & (ip.packed[i >> 3] >> 7 - (i % 8))))
            i += 1
            if i == 16:
                self.v6offsetCache[key] = node

        return node

    def read_node(self, node, idx):
        off = idx * 4 + node * 8
        return bytes2long(self.data[off], self.data[off + 1], self.data[off + 2], self.data[off + 3])

    def _resolve(self, node):
        resolved = node - self.meta.node_count + self.meta.node_count * 8
        size = bytes2long(0, 0, self.data[resolved], self.data[resolved + 1])
        return self.data[resolved+2:resolved+2 + size]

    def find(self, addr, language = "CN"):
        node = self._find_node(ipaddress.ip_address(addr))
        if node is None:
            return None

        bytes = self._resolve(node)
        if bytes is None:
            return None

        tmp = bytes.decode("utf-8").split("\t")

        off = self.meta.languages.get(language)
        if off is None:
            return None

        return tmp[off:off+len(self.meta.fields)]

    def find_map(self, addr, language = 'CN'):
        loc = self.find(addr, language)
        if loc is None:
            return None
        m = {}
        for idx, value in enumerate(self.meta.fields):
            m[value] = loc[idx]
        return m

    def find_info(self, addr, language = 'CN'):
        m = self.find_map(addr, language)
        if m is None:
            return None
        return IPInfo(**m)