import streamlit as st
from streamlit_option_menu import option_menu

# Configuración de la página
st.set_page_config(page_title="Aplicación con Dropdown", layout="wide")

# Barra de navegación con opciones
with st.container():
    selected = option_menu(
        menu_title="Menú de Navegación",  # Título del menú
        options=["Inicio", "Acerca de", "Servicios", "Más"],  # Opciones del menú principal
        icons=["house", "info-circle", "briefcase", "three-dots"],  # Íconos de cada opción
        menu_icon="cast",  # Icono general del menú
        default_index=0,  # Opción seleccionada por defecto
        orientation="horizontal",  # Menú horizontal
    )

# Mostrar el contenido según la opción seleccionada
if selected == "Inicio":
    st.title("Bienvenido a la página de Inicio")
    st.write("Contenido de la página de inicio.")
elif selected == "Acerca de":
    st.title("Acerca de nosotros")
    st.write("Información sobre la aplicación.")
elif selected == "Servicios":
    st.title("Nuestros Servicios")
    st.write("Descripción de los servicios.")
elif selected == "Más":
    st.title("Menú Más")
    st.write("Elige una subopción:")
    
    # Crear un selectbox para el submenú
    subselected = st.selectbox("Selecciona una subopción", ["Subopción 1", "Subopción 2", "Subopción 3"])
    st.write(f"Has seleccionado {subselected}")
