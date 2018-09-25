# ipdb-python
IPIP.net officially supported IP database ipdb format parsing library

# Python Parse ipdb file

## Installing
<pre>
<code>pip install ipip-ipdb</code>
</pre>

## Dependents ( python 2.x )
<pre><code>pip install ipaddress</code></pre>

## Code Example
  <pre><code>
import ipdb

db = ipdb.Reader("/path/to/mydatatest.ipdb")
print(db.find("2001:250:200::"))
print(db.find_map("2001:250:200::"))

info = db.find_info("2a06:e881:3800::")
print(info.country_name, info.region_name, info.city_name, info.owner_domain, info.isp_domain, info.latitude, info.longitude, info.timezone, info.utc_offset)
  </pre></code>
