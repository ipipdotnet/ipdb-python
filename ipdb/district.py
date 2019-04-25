# -*- coding: utf-8 -*-
"""
    :copyright: ©2018 by IPIP.net
"""

from .database import Database


class DistrictInfo:
    country_name = ""
    region_name = ""
    city_name = ""
    district_name = ""
    china_admin_code = ""
    covering_radius = ""
    latitude = ""
    longitude = ""

    def __init__(self, **kwargs):
        self._map = kwargs
        for key in self._map:
            self.__dict__[key] = self._map[key]


class District(Database):

    info = DistrictInfo
