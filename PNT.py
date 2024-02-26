import phonenumbers
from phonenumbers import geocoder
from test import number
import folium

check_number = phonenumbers.parse("+91**********")
number_location = geocoder.description_for_number(check_number, "en")
print(number_location)


from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

