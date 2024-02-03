import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
import webbrowser
import folium
from opencage.geocoder import OpenCageGeocode
from os.path import dirname
import os
 
number = input("Enter the PhoneNumber with the country code : ")
try:
    phoneNumber = phonenumbers.parse(number)
except:
    print("Something went wrong. ")
    quit()

Key = "d663b90529b84edabd83bb15fa58efe9"

is_possible_number = phonenumbers.is_possible_number()
is_valid_number = phonenumbers.is_valid_number()
if not (is_possible_number and is_valid_number):
    print("The number provided is not valid. Please try another number. ")
    quit()
else:
    print("Valid number!")


yourLocation = geocoder.description_for_number(phoneNumber,"en")
print("Location: "+yourLocation)

yourServiceProvider = carrier.name_for_number(phoneNumber,"en")
print("service provider: "+yourServiceProvider)
 
geocoder = OpenCageGeocode(Key)
query = str(yourLocation)
results = geocoder.geocode(query)
 
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
 
myMap = folium.Map(loction=[lat,lng],zoom_start = 9)
 
folium.Marker([lat,lng],popup=yourLocation).add_to(myMap)
 
myMap.save("Location.html")
webbrowser.open('file://' + os.path.realpath("Location.html"))

