# -*- coding: utf-8 -*-
"""
    :copyright: ©2018 by IPIP.net
"""

class ASNInfo:
    asn = -1
    reg = ""
    cc = ""
    net = ""
    org = ""

    def __init__(self, **kwargs):
        self._map = kwargs
        for key in self._map:
            self.__dict__[key] = self._map[key]

    def get_number(self):
        return self.asn

    def get_registry(self):
        return self.reg

    def get_country(self):
        return self.cc

    def get_net_name(self):
        return self.net

    def get_organization(self):
        return self.org
