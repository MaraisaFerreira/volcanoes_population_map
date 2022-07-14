import folium
import pandas as pd

map = folium.Map(
    location=[40.14622260307797, -104.32315718977355],
    zoom_start=4.2,
)

df_volcanoes = pd.read_csv("Volcanoes.txt")
volcanoes_name = list(df_volcanoes["NAME"])
volcanoes_lat = list(df_volcanoes["LAT"])
volcanoes_lon = list(df_volcanoes["LON"])
volcanoes_elev = list(df_volcanoes["ELEV"])

volcanoes = zip(volcanoes_name, volcanoes_lat, volcanoes_lon, volcanoes_elev)


def get_color(el):
    if el < 1500:
        return "green"
    elif 1500 <= el < 3000:
        return "orange"
    else:
        return "red"


fg_volcanoes = folium.FeatureGroup("Volcanoes")
for name, lat, lon, elev in volcanoes:
    iframe = folium.IFrame(
        html=f"<strong>Volcano name:</strong> {name}<br>\
        <strong>Height:</strong> {elev}m",
        width=200,
        height=100,
    )
    fg_volcanoes.add_child(
        folium.CircleMarker(
            location=[lat, lon],
            popup=folium.Popup(iframe),
            radius=6,
            color="grey",
            fill_color=get_color(elev),
            fill_opacity=0.8,
        )
    )

fg_population = folium.FeatureGroup("Population")
fg_population.add_child(
    folium.GeoJson(
        data=open("world.json", "r", encoding="utf-8-sig").read(),
        style_function=lambda x: {
            "fillColor": "green"
            if x["properties"]["POP2005"] < 100000000
            else "orange"
            if 100000000 <= x["properties"]["POP2005"] < 250000000
            else "red",
            'color': 'gray'
        },
    )
)

map.add_child(fg_volcanoes)
map.add_child(fg_population)
map.add_child(folium.LayerControl())
map.save("FirstMap.html")
