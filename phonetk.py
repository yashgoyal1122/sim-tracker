import phonenumbers
import folium
from numb import number

from phonenumbers import geocoder
Country_Code_Number = phonenumbers.parse(number,"CN")
print(Country_Code_Number)
location = (geocoder.description_for_number(Country_Code_Number,'en'))
print(location)

from phonenumbers import carrier
print(carrier.name_for_number(Country_Code_Number,"en"))

from opencage.geocoder import OpenCageGeocode
key = '03cac31db78748d0944c8f1eb39348f9'
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat,lng)

myMap = folium.Map(location = [lat,lng], zoom_start=9)
folium.Marker([lat,lng], popup= location).add_to(myMap)
myMap.save("mylocation.html")
