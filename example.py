from  __future__ import unicode_literals
import ipdb,sys

import pandas as pd

def test_city_district():
    db = ipdb.City("c:/work/ipdb/test.ipdb")
    print(db.fields())
    city = db.find_info(u"111.199.81.160", "CN")
    qx = city.get_district()
    if qx != None:
        print(qx.city_name, qx.district_name)

def test_free():
    db = ipdb.City("c:/work/ipdb/mydata4vipweek2.ipdb")
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
    db = ipdb.City("c:/tiantexin/download/mydata4vipday4_cn.ipdb")
    print(db.is_ipv4(), db.is_ipv6())
    print(db.languages())
    print(db.fields())
    print(db.build_time())
    print(db.find("1.1.1.1", "CN"))
    print(db.find_map("8.8.8.8", "CN"))
    print(db.find_info("118.28.1.1", "CN").country_name)

import  ipaddress

def test_city_ipv6_test():

    db = ipdb.City("c:/work/ipdb/mydata6vipday2.ipdb")

    print(db.find("2001:44c8:4644:1191:3c41:724d:e391:51b0", "CN"))
    print(db.find_map("2a04:3543:1000:2310:ecb3:3eff:fef0:20e1", "CN"))
    print(db.find_info("2a04:3543:1000:2310:ecb3:3eff:fef0:20e1", "CN").country_name)

def test_city_ipv6():
    db4 = ipdb.City("c:/tiantexin/download/mydata4vipday4_cn.ipdb")
    db = ipdb.City("c:/work/ipdb/mydata6vipday2.ipdb")

    df = pd.read_csv("C:\\Users\\GAOCHUNHUI\\Documents\\WeChat Files\\daxime\\FileStorage\\File\\2019-10\\ipiptest\\ip_data.csv")
    for i, row in df.iterrows():
        if ipaddress.ip_address(row['request_ip']).version == 4:

            db4.find(row['request_ip'], "CN")
        else:
            print(db.find(row['request_ip'], "CN"), row['request_ip'])

    try:
        print(db.find("2000:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF", "CN"))
    except Exception as e:
        print(e)


def test_district():
    db = ipdb.District("c:/work/ipdb/china_district.ipdb")
    print(db.is_ipv4(), db.is_ipv6())
    print(db.languages())
    print(db.fields())
    print(db.build_time())
    for A in range(223):
        for B in range (255):
            try:
                print(db.find("%d.%d.114.144" % (A, B), "CN"))
            except ipdb.IPNotFound as e:
                print(e)

    try:
        print(db.find("1.1.1.1", "CN"))
    except ipdb.IPNotFound as e: # ip not found
        print(e)
    except ipdb.DatabaseError as e: # database file size error
        print(e)
    print(db.find_map("1.12.13.255", "CN"))
    print(db.find_info("1.12.13.255", "CN").country_name)


def test_base_station():
    db = ipdb.BaseStation("c:/work/ipdb/base_station.ipdb")
    print(db.is_ipv4(), db.is_ipv6())
    print(db.languages())
    print(db.fields())
    print(db.build_time())
    print(db.find_map("117.136.83.55", "CN"))


def test_idc_list():
    db = ipdb.IDC("c:/work/ipdb/idc_list.ipdb")
    print(db.find_map("1.1.1.1", "CN"))
    print(db.find_map("8.8.8.8", "CN"))

# test_city_ipv4()
# test_city_ipv6_test()
# test_base_station()
test_city_district()
# test_city_ipv4()