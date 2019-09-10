from  __future__ import unicode_literals
import ipdb_py,sys



def test_free():
    db = ipdb_py.City("c:/work/ipdb/mydata4vipweek2.ipdb")
    print(db.is_ipv4(), db.is_ipv6())
    print(db.languages())
    print(db.fields())
    print(db.build_time())
    print(db.find("1.1.1.1", "CN"))

    print("ipdb reload", db.reload("c:/work/ipdb/city.free.ipdb"))
    print(db.find("118.28.1.1", "CN"))


    try:
        print(db.find("2000:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF", "CN"))
    except Exception as e:
        print(e)


def test_city_ipv4():
    db = ipdb_py.City("c:/tiantexin/download/mydata4vipday4_cn.ipdb")
    print(db.is_ipv4(), db.is_ipv6())
    print(db.languages())
    print(db.fields())
    print(db.build_time())
    print(db.find("1.1.1.1", "CN"))
    print(db.find_map("8.8.8.8", "CN"))
    print(db.find_info("118.28.1.1", "CN").country_name)


def test_city_ipv6():
    db = ipdb_py.City("c:/work/ipdb/city.ipv6.ipdb")
    print(db.is_ipv4(), db.is_ipv6())
    print(db.languages())
    print(db.fields())
    print(db.build_time())
    print(db.find("2001:250:200::", "CN"))

    try:
        print(db.find("2000:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF", "CN"))
    except Exception as e:
        print(e)


def test_district():
    db = ipdb_py.District("c:/work/ipdb/china_district.ipdb")
    print(db.is_ipv4(), db.is_ipv6())
    print(db.languages())
    print(db.fields())
    print(db.build_time())
    for A in range(223):
        for B in range (255):
            try:
                print(db.find("%d.%d.114.144" % (A, B), "CN"))
            except ipdb_py.IPNotFound as e:
                print(e)

    try:
        print(db.find("1.1.1.1", "CN"))
    except ipdb_py.IPNotFound as e: # ip not found
        print(e)
    except ipdb_py.DatabaseError as e: # database file size error
        print(e)
    print(db.find_map("1.12.13.255", "CN"))
    print(db.find_info("1.12.13.255", "CN").country_name)


def test_base_station():
    db = ipdb_py.BaseStation("c:/work/ipdb/base_station.ipdb")
    print(db.is_ipv4(), db.is_ipv6())
    print(db.languages())
    print(db.fields())
    print(db.build_time())
    print(db.find_map("117.136.83.55", "CN"))


def test_idc_list():
    db = ipdb_py.IDC("c:/work/ipdb/idc_list.ipdb")
    print(db.find_map("1.1.1.1", "CN"))
    print(db.find_map("8.8.8.8", "CN"))

# test_city_ipv4()
# test_city_ipv6()
# test_base_station()
test_district()
# test_city_ipv4()