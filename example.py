import ipdb,sys

db = ipdb.Reader("c:/work/tiantexin/bb/v6/mydata6vipday4.ipdb")

print(db.support_languages())

try:
    print(db.find("2000:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF", "CN"))
except Exception as e:
    print(e)

sys.exit(0)
print(db.find_map("2001:250:201::"))

info = db.find_info("2a06:e881:3800::")
print(info.country_name, info.region_name, info.city_name, info.owner_domain, info.isp_domain, info.latitude, info.longitude, info.timezone, info.utc_offset)
