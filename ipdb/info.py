# -*- coding: utf-8 -*-
"""
    :copyright: ©2018 by IPIP.net
"""


class IPInfo(object):
    
    country_name = ""
    region_name = ""
    city_name = ""
    owner_domain = ""
    isp_domain = ""
    latitude = ""
    longitude = ""
    timezone = ""
    utc_offset = ""
    china_admin_code = ""
    idd_code = ""
    country_code = ""
    continent_code = ""
    idc = ""
    base_station = ""
    country_code3 = ""
    european_union = ""
    currency_code = ""
    currency_name = ""
    anycast = ""

    def __init__(self, **kwargs):
        self._map = kwargs
        for key in self._map:
            self.__setattr__(key, self._map[key])

    def __getattr__(self, item):
        return self._map.get(item, "")
