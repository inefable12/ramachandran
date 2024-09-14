import streamlit as st
#from RamachanDraw import fetch, phi_psi, plot
import matplotlib.pyplot as plt
from ramachandraw.parser import get_phi_psi
from ramachandraw.utils import fetch_pdb 
from ramachandraw.utils import plot

st.title("Generador del Diagrama de Ramachandran")

pdb_id = st.text_input("Escribe el código de 4 dígitos: ", "3PL1")
# Draw the Ramachandran plot
pdb_file = fetch_pdb(pdb_id))
# Generate a dictionary to store the (phi, psi) torsion angles
#torsion_angles = get_phi_psi(fetch_pdb(pdb_id))

plt.figure()
    plot(pdb_file)

st.markdown("### Ramachandran Plot of given Protein: ")
    st.pyplot()
