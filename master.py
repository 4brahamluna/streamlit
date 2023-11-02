import streamlit as st
import matplotlib.pyplot as plt
import folium


st.set_page_config(page_title="Meu Site StreamLit")

st.title("Dashboard de Rotas")

st.write("Meu primeiro site com o Streamlit")

# Importar os dados do mapa
dados_mapa = pd.read_csv("dados_mapa.csv")

# Criar um mapa do Rio Grande do Norte
mapa = folium.Map(location=[-5.18, -36.94], zoom_start=7)

# Adicionar os municípios do Rio Grande do Norte ao mapa
for municipio in dados_mapa.itertuples():
    folium.Marker([municipio.latitude, municipio.longitude], popup=municipio.nome).add_to(mapa)

# Exibir o mapa
st.write(mapa)
