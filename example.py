import ipdb

db = ipdb.Reader("C:/WORK/tiantexin/framework/library/ip/mydata6.ipdb")
print(db.find("2001:250:200::"))
print(db.find_map("2001:250:200::"))

info = db.find_info("2a06:e881:3800::")
print(info.country_name, info.region_name, info.city_name, info.owner_domain, info.isp_domain, info.latitude, info.longitude, info.timezone, info.utc_offset)