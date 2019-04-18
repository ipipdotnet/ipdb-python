import unittest

import ipdb

class TestIPDb(unittest.TestCase):

    def test_city(self):
        print("\n\ntest city start\n\n")
        city = ipdb.City("c:/work/ipdb/city.ipv4.ipdb")
        print("ipdb.build.time:", city.build_time())
        for A in range(224):
            ip_address = u"%d.28.1.1" % A
            print(ip_address, city.find(ip_address, "CN"))
            print(ip_address, city.find_map(ip_address, "CN"))
            print(ip_address, city.find_info(ip_address, "CN"))

        print("\n\ntest city start\n\n")

    def test_district(self):
        print("\n\ntest district start\n\n")
        district = ipdb.District("c:/work/ipdb/china_district.ipdb")
        print("ipdb.build.time:", district.build_time())
        for A in range(224):
            ip_address = u"%d.28.1.1" % A
            try:
                print(ip_address, district.find(ip_address, "CN"))
                print(ip_address, district.find_map(ip_address, "CN"))
                print(ip_address, district.find_info(ip_address, "CN"))
            except ipdb.IPNotFound as e:
                print(ip_address, e)
        print("\n\ntest district end\n\n")

    def test_station(self):
        print("\n\ntest base_station start\n\n")
        base_station = ipdb.BaseStation("c:/work/ipdb/base_station.ipdb")
        print("ipdb.build.time:", base_station.build_time())
        for A in range(224):
            ip_address = u"%d.28.1.1" % A
            try:
                print(ip_address, base_station.find(ip_address, "CN"))
                print(ip_address, base_station.find_map(ip_address, "CN"))
                print(ip_address, base_station.find_info(ip_address, "CN"))
            except ipdb.IPNotFound as e:
                print(ip_address, e)
        print("\n\ntest base_station end\n\n")


if __name__ == "__main__":
    unittest.main()