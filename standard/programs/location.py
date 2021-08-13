from requests import get
import os

ip = get('https://api.ipify.org').text

import IP2Location

database = IP2Location.IP2Location(os.path.join("data", "IPV4-COUNTRY.BIN"))

rec = database.get_all(ip)

print(rec.country_short)
print(rec.country_long)
print(rec.region)
print(rec.city)
print(rec.isp)  
print(rec.latitude)
print(rec.longitude)            
print(rec.domain)
print(rec.zipcode)
print(rec.timezone)
print(rec.netspeed)
print(rec.idd_code)
print(rec.area_code)
print(rec.weather_code)
print(rec.weather_name)
print(rec.mcc)
print(rec.mnc)
print(rec.mobile_brand)
print(rec.elevation)
print(rec.usage_type)