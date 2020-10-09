import googlemaps
import pprint
import webbrowser
import os

pp = pprint.PrettyPrinter(indent=2)


api_key = 'AIzaSyCFv52MzJAFk2vefN2sGX9z_aoy9G9OV_0'

address = '1357 Pinewood Rd, Jacksonville Beach, Fl'

gmaps = googlemaps.Client(key=api_key)
gbr = gmaps.geocode(address)

# crd = {lat: some_latitue, lng: some_longitude}
crd = gbr[0]['geometry']['location']

# find places within 5km of the address
gbrnb = gmaps.places_nearby(crd, radius=10000)

photos = []
imgs = []
for r in gbrnb['results'] : 
	for p in r['photos'] :
		photos.append(p)

pt = 'https://maps.googleapis.com/maps/api/place/photo?photoreference={photo_reference}&sensor=false&maxheight={height}&maxwidth={width}&key='+api_key

for p in photos :
	imgs.append( pt.format( photo_reference = p["photo_reference"], width = p["width"], height=p["height"]) )

f = open("near_me.html", "w")
f.write("<html><head><title>Near "+address+"</title><style>nm {margin-bottom:15px;}</style></head><body>")
for x, i in enumerate(imgs) :
	f.write("\t"+("".join(photos[x]["html_attributions"]))+"<br/>\n"  )
	f.write("\t<img src=\"{img}\" height=\"300\" class=\"nm\"/><br/>\n".format(img=i));
f.write("\n</body>\n</html>")
f.close()

url = p = "file://"+os.path.realpath("near_me.html")
webbrowser.open(url)
