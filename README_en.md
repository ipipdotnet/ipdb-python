# ipdb-python
IPIP.net officially supported IP database ipdb format parsing library

# Python Parse ipdb file

## Installing
<pre>
<code>pip install ipip-ipdb</code>
</pre>

## Dependents ( python 2.x or before python 3.3 )
<pre><code>pip install ipaddress</code></pre>

## Code Example
  <pre><code>
import ipdb

db = ipdb.City("/path/to/city.ipv4.ipdb")
# db.reload("/path/to/city.ipv4.ipdb") # update ipdb database file reload data
print(db.is_ipv4(), db.is_ipv6())
print(db.languages()) # support language
print(db.fields()) #  support fields
print(db.build_time()) #  build database time
print(db.find("1.1.1.1", "CN")) #  query ip return array
# print(db.find(u"1.1.1.1", "CN")) #  Python 2.7
print(db.find_map("8.8.8.8", "CN")) #  query ip return dict
print(db.find_info("118.28.1.1", "CN").country_name) 
  </pre></code>

### IPDB Database Fields:
<pre>
country_name : Country Name 
region_name  : Province Name   
city_name    : City Name 
owner_domain : Domain of IP owner
isp_domain  :  ISP of IP being broadcasted
latitude  :  Latitude   
longitude : Longitude    
timezone : Timezone     
utc_offset : UTC time standard offset    
china_admin_code : China administrative divisions code
idd_code : International Dialling Codes 
country_code : Two-letter country codes based on ISO 3166. 
continent_code : Regional Internet registry code.   
idc : IDC label
base_station : Basestation label
country_code3 : Three-letter country codes based on ISO 3166.
european_union : European union label
currency_code : Currency Code    
currency_name : Currency Name
anycast : ANYCAST label      

</pre>

### IPDB CN District sample code :
  <pre>
import ipdb

db = ipdb.District("/path/to/china_district.ipdb")
print(db.is_ipv4(), db.is_ipv6())
print(db.languages())
print(db.fields())
print(db.build_time())
print(db.find("1.12.13.255", "CN"))
print(db.find_map("1.12.13.255", "CN"))
print(db.find_info("1.12.13.255", "CN").country_name)
  </pre>

### IPDB Basestation sample code :
<pre>
import ipdb
db = ipdb.BaseStation("/path/to/base_station.ipdb")
print(db.is_ipv4(), db.is_ipv6())
print(db.languages())
print(db.fields())
print(db.build_time())
print(db.find_map("117.136.83.55", "CN"))
</pre>