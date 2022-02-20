import osmapi

#create the api object
api = osmapi.OsmApi()

#get a node from the api with a specified id and print it
print(api.NodeGet(123))
