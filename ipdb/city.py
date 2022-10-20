# -*- coding: utf-8 -*-
"""
    :copyright: ©2018 by IPIP.net
"""

from .database import Reader
from .district import DistrictInfo
from .asn import ASNInfo

import json

class CityInfo:
    country_name = ""
    region_name = ""
    city_name = ""
    district_name = ""
    owner_domain = ""
    isp_domain = ""
    latitude = ""
    longitude = ""
    timezone = ""
    utc_offset = ""
    china_region_code = ""
    china_city_code = ""
    china_district_code = ""
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
    line = ""
    usage_type = ""
    district_info = ""
    route = ""
    asn = ""
    asn_info = ""

    def __init__(self, **kwargs):
        self._map = kwargs
        for key in self._map:
            self.__dict__[key] = self._map[key]

    def get_district(self):
        if len(self.district_info) == 0:
            return None
        o = json.loads(self.district_info)
        o["country_name"] = self.country_name
        o["region_name"] = self.region_name
        o["city_name"] = self.city_name
        return DistrictInfo(**o)

    def get_asninfo(self):
        if len(self.asn_info) == 0:
            return None
        ls = json.loads(self.asn_info)
        result = []
        for i in ls:
            result.append(ASNInfo(**i))

        return result


class City:

    db = None

    def __init__(self, name):
        self.db = Reader(name)

    def reload(self, name):
        try:
            db = Reader(name)
            self.db = db
            return True
        except:
            return False            

    def find(self, addr, language):
        return self.db.find(addr, language)

    def find_map(self, addr, language):
        return self.db.find_map(addr, language)

    def find_info(self, addr, language):
        m = self.db.find_map(addr, language)
        if m is None:
            return None
        return CityInfo(**m)

    def is_ipv4(self):
        return self.db.is_support_ipv4()

    def is_ipv6(self):
        return self.db.is_support_ipv6()

    def languages(self):
        return self.db.support_languages()

    def fields(self):
        return self.db.support_fields()

    def build_time(self):
        return self.db.build_utc_time()
