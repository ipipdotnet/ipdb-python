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
print(db.find_map("8.8.8.8", "CN")) #  query ip return dict
print(db.find_info("118.28.1.1", "CN").country_name) 
  </pre></code>
