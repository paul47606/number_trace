import phonenumbers
from phonenumbers import geocoder

key = '68f0c1ea117242e0868873e7cc7942c3'# To update the API address in your key, you can obtain the necessary information by visiting the website opencagedata.com.
number = ""

ch_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(ch_number, "en"))

# to get service provider number

from phonenumbers import carrier

serivice_provider = phonenumbers.parse(number)
print(carrier.name_for_number(serivice_provider, "en"))

# to find latitude and longitude by using geocoder

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)
query = str(ch_number)
results = geocoder.geocode(query)

print(results)
