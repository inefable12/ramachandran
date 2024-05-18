import streamlit as st
from RamachanDraw import fetch, phi_psi, plot
import matplotlib.pyplot as plt


# Set Streamlit configurations
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(page_title="Generador del Diagrama de Ramachandran", page_icon=":heart:")


# Show the introduction text
st.text(
    'Esta aplicación web fue desarrollada por Mohit Poudel y se encuentra disponible en su versión original en: https://mohit254-rc-plot-streamlit-app-gsua5l.streamlit.app/ y está diseñada para ayudar a investigadores y científicos a obtener el diagrama de Ramachandran a través de la identificación de la base de datos de proteínas (ID de PDB).')

st.title("Ramachandran Plot Generator")

st.markdown('''
Un diagrama de Ramachandran es una representación gráfica de las conformaciones de péptidos y proteínas en función de los valores de sus ángulos phi y psi. 

Phi y psi son ángulos diédricos que describen la conformación de la cadena principal de una proteína. 

El ángulo phi se define como el ángulo entre el plano formado por los átomos N-C alfa-C y el plano formado por los átomos C alfa-N-C. 

El ángulo psi se define como el ángulo entre el plano formado por los átomos C alfa-N y el plano formado por los átomos N-C alfa-C. 

Los gráficos de Ramachandran se utilizan a menudo para analizar la flexibilidad conformacional de las proteínas y para identificar regiones de una proteína que son propensas a perturbaciones estructurales. 

También se utilizan para identificar anomalías estructurales y predecir las conformaciones de bucles de proteínas. 

Los gráficos de Ramachandran generalmente se generan trazando los ángulos phi en el eje x y los ángulos psi en el eje y. 

La gráfica resultante se divide en regiones, correspondiendo cada región a un tipo diferente de conformación de proteína.

''')

# Option to choose between PDB or mmCIF file formats
file_format = st.selectbox("Escoge el formato de tu archivo:", options=["PDB", "mmCIF"])

if file_format == "PDB":
    st.markdown("##### Ingresa el identificador PDB: ")
    # PDB id to be downloaded
    PDB_id = st.text_input("Escribe el código de 4 dígitos: ", "3PL1")
    if PDB_id:
        # Fetch the PDB file for the given ID
        pdb_file = fetch(PDB_id)

elif file_format == "mmCIF":
    st.markdown("##### Ingresa el archivo mmCIF: ")
    # mmCIF file to be uploaded
    uploaded_file = st.file_uploader("Escoge el archivo mmCIF", type=["cif", "mmcif"])
    if uploaded_file:
        pdb_file = uploaded_file.read().decode("utf-8")

if 'pdb_file' in locals():
    # Generate the plot using Matplotlib

    plt.figure()
    plot(pdb_file)


    # Display the plot in the Streamlit app using st.pyplot
    st.markdown("### Diagrama de Ramachandran de la Proteína ingresada: ")
    st.pyplot()


# --- HERO SECTION ---
st.markdown("## Contacto: ")
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQrz4fkFh7FwQ498chHBA-W5TWC4Uk0fAt7oEAQ8zLCUA&s",
        #https://media.licdn.com/dms/image/C4E03AQGwZ6UAzv6-fw/profile-displayphoto-shrink_200_200/0/1619592173009?e=1682553600&v=beta&t=1dTWbkIKGSnmD8TUUPhCkT9p9Dtu3NXmJLNlaCUyX0A",
        width=230)

with col2:
    st.title("Jesus Alvarado")
    st.write("Docente universitario, investigador y divulgador de talleres STEAM") #Bioinformatics & population genetics enthusiast, self-taught python programmer")
    st.write("Simulaciones Computacionales y Machine Learning")
    st.write("Lima, Perú")

# st.markdown("# Mohit Poudel")
# st.markdown("### Research Intern at the Centre for Biotechnology, Agriculture and Forestry University,Nepal")
st.markdown("#### Email: inefable12@gmail.com ")
st.markdown(
    "##### [Investigaciones](https://scholar.google.es/citations?hl=es&user=hhUz0WAAAAAJ&view_op=list_works&sortby=pubdate)")
    #https://mohit254-portfolio-cv-t4bwqw.streamlit.app/#mohit-poudel)")
