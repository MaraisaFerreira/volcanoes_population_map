import folium

map = folium.Map(
    location=[40.689900213736635, -74.04441456931458],
    zoom_start=5,
    tiles="Stamen Terrain",
)

map.save("FirstMap.html")
