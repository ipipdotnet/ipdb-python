# -*- coding: utf-8 -*-
"""
    :copyright: ©2018 by IPIP.net
"""

from .database import Database


class CityInfo:
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
            self.__dict__[key] = self._map[key]


class City(Database):

    info = CityInfo
