import googlemaps
from datetime import datetime

# You have to enable API uasge https://console.cloud.google.com/apis/library?project=cedar-oath-273816

if __name__ == '__main__':
    gmaps = googlemaps.Client(key='AIzaSyCLVTBtdcceVqe-JkM83xvl1y5yOtBhIWw')

    # Geocoding an address
    geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

    # Look up an address with reverse geocoding
    reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

    # Request directions via public transit
    now = datetime.now()
    directions_result = gmaps.directions("Sydney Town Hall",
                                         "Parramatta, NSW",
                                         mode="transit",
                                         departure_time=now)


