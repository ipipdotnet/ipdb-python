# -*- coding: utf-8 -*-
"""
    :copyright: ©2018 by IPIP.net
"""


class MetaData(object):
    def __init__(self, **kwargs):
        self.fields = kwargs['fields']
        self.node_count = kwargs['node_count']
        self.total_size = kwargs['total_size']
        self.build = kwargs['build']
        self.languages = kwargs['languages']
        self.ip_version = kwargs['ip_version']