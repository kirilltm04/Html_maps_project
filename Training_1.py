from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="PyCharm")
location = geolocator.geocode("Fishkill, New York, USA")
print((location.latitude, location.longitude))
