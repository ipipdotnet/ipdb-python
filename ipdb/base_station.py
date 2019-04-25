# -*- coding: utf-8 -*-
"""
    :copyright: ©2018 by IPIP.net
"""

from .database import Database


class BaseStationInfo:
    country_name = ""
    region_name = ""
    city_name = ""
    owner_domain = ""
    isp_domain = ""
    base_station = ""

    def __init__(self, **kwargs):
        self._map = kwargs
        for key in self._map:
            self.__dict__[key] = self._map[key]


class BaseStation(Database):

    info = BaseStationInfo
