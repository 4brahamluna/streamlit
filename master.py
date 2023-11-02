import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Importa os dados do mapa do Rio Grande do Norte
data = np.loadtxt("mapa_rn.csv", delimiter=",")

# Cria um mapa do Rio Grande do Norte
fig, ax = plt.subplots(1, 1)
ax.imshow(data)

# Adiciona um título ao mapa
ax.set_title("Mapa do Rio Grande do Norte")

# Adiciona um widget de seleção de dados
point = st.selectbox("Selecione um ponto do mapa", data[:, 0], data[:, 1])

# Mostra informações sobre o ponto selecionado
st.write("O ponto selecionado é:", point)
