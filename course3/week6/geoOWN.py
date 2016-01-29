# Access the Local copy of the GEO api
import urllib
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson?'

while True:
    # Enter address
    address = raw_input("Enter Location: ")
    if len(address) < 1 : break

    # Read data
    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print "Retrieving", url
    data = urllib.urlopen(url).read()
    print "Retrieved", len(data), 'characters'

    # Get Place ID
    dataJS = json.loads(data)
    print "Place id", dataJS["results"][0]["place_id"]
