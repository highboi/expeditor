import overpy

#make the overpass api object
api = overpy.Overpass()

#send a query to openstreetmap in overpassql language
result = api.query("""
	way(50.746,7.154,50.748,7.157) ["highway"];
	(._;>;);
	out body;
""")

#print all of the ways returned by the server
for way in result.ways:
	print(way)
