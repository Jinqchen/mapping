import folium
import pandas
data = pandas.read_csv("volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
name=list(data["NAME"])
map=folium.Map(location=[40.916908965758296, -73.12485183064408],title="Stamen Terrain")
fg=folium.FeatureGroup(name="My Map")
for la,ln,nm in zip(lat,lon,name):
    fg.add_child(folium.Marker(location=[la, ln],popup=nm,icon=folium.Icon(color="green")))
    map.add_child(fg)
map.save("Map1.html")
