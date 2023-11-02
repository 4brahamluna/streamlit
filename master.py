import streamlit as st
import matplotlib.pyplot as plt
import folium
import requests

# Importar os dados do mapa
dados_mapa = pd.read_csv("mapa_rn.csv")

# Criar um mapa do Rio Grande do Norte
mapa = folium.Map(location=[-5.18, -36.94], zoom_start=7)

# Adicionar os municípios do Rio Grande do Norte ao mapa
for municipio in dados_mapa.itertuples():

    # Fazer uma solicitação HTTP ao site do IBGE
    resposta = requests.get(f"https://geoftp.ibge.gov.br/mapas/bases_cartograficas/malhas_municipais/municipios_2023/png/{municipio.ibge}.png")

    # Armazenar a imagem na memória
    imagem = resposta.content

    # Adicionar a imagem ao mapa
    folium.Marker([municipio.latitude, municipio.longitude], popup=municipio.nome, icon=folium.Icon(image=imagem)).add_to(mapa)

# Exibir o mapa
st.write(mapa)
