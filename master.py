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

# Mostra o mapa
st.pyplot(fig)
