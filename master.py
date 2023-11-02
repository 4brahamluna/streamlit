import folium
import streamlit as st

from streamlit_folium import st_folium

# center on Liberty Bell, add marker
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
folium.Marker(
    [39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell"
).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)

{
"last_clicked":NULL
"last_object_clicked":NULL
"last_object_clicked_tooltip":NULL
"last_object_clicked_popup":NULL
"all_drawings":NULL
"last_active_drawing":NULL
"bounds":{
"_southWest":{
"lat":39.94384773921137
"lng":-75.15805006027223
}
"_northEast":{
"lat":39.9553624980935
"lng":-75.14249324798585
}
}
"zoom":16
"last_circle_radius":NULL
"last_circle_polygon":NULL
"center":{
"lat":39.94961
"lng":-75.150282
}
}
