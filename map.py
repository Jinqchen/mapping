import folium
import pandas
data = pandas.read_csv("volcanoes.txt")
lat=list(data["LAT"])
lon=list(data["LON"])
name=list(data["NAME"])
elev=list(data['ELEV'])
html = """
Volcano name:<br> 
<a href="https://www.google.com/search?q=%s\" target="_blank">%s</a><br>
Height: %s m
"""

map=folium.Map(location=[40, -73],title="Stamen Terrain")
fg=folium.FeatureGroup(name="My Map")
for la,ln,name,el in zip(lat,lon,name,elev):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)
    fg.add_child(folium.Marker(location=[la, ln],popup=folium.Popup(iframe),icon=folium.Icon(color="green")))
    map.add_child(fg)
map.save("Map1.html")
