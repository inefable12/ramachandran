import streamlit as st
import matplotlib.pyplot as plt
from ramachandraw.parser import get_phi_psi
from ramachandraw.utils import fetch_pdb 
from ramachandraw.utils import plot

st.title("Generador de Diagrama de Ramachandran")
st.text("Autor: Jesús Alvarado")

pdb_id = st.text_input("Escribe el código PDB de 4 dígitos, por ejemplo: ", "3PL1")
pdb_file = fetch_pdb(pdb_id)

plt.figure()
#fig, ax = plt.subplots()
plot(pdb_file)#, ax=ax) 

st.markdown("**Resultado :gift:**")
st.pyplot()
st.balloons(plt.gcf())
