import streamlit as st
#from RamachanDraw import fetch, phi_psi, plot
import matplotlib.pyplot as plt
from ramachandraw.parser import get_phi_psi
from ramachandraw.utils import fetch_pdb 
from ramachandraw.utils import plot

st.title("Generador de Diagrama de Ramachandran")
st.text("Autor: Jesus Alvarado")

pdb_id = st.text_input("Escribe el código PDB de 4 dígitos, por ejemplo: ", "3PL1")
pdb_file = fetch_pdb(pdb_id)

plt.figure()
plot(pdb_file)
st.markdown("Resultado :gift:")
st.pyplot()
