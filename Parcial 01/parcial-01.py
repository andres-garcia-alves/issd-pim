import io
import numpy as np
import cv2
from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu

# otra opción ...
# def on_change(key):
#   st.write(f"Selection changed to { st.session_state[key] }")
#   main_menu_2 = option_menu(key='menu_5', menu_title='', options=["Home", "Upload", "Tasks", 'Settings'],
#     icons=['house', 'cloud-upload', "list-task", 'gear'], orientation="horizontal", on_change=on_change)

st.set_page_config(
  page_title='ISSD | PIM',
  page_icon='https://raw.githubusercontent.com/andres-garcia-alves/issd-pim/refs/heads/main/Parcial%2001/issd.png',
  layout='wide'
)

# funcion para construir el menu principal
def get_main_menu():
  menu_options = ['Escalado', 'Rotación', 'Traslación', 'Grises', 'Suavizado Blur', 'Suavizado Gausiano', 'Bordes Sobel', 'Bordes Canny']
  menu_icons = ['house', 'cloud-upload', 'list-task', 'gear']
  menu_styles = []
  menu_styles2 = {
        "container": { "padding": "0!important", "background-color": "#fafafa" },
        "icon": { "color": "black", "font-size": "18px" },
        "nav-link": { "font-size": "16px", "text-align": "center", "margin": "0px" },
        "nav-link-selected": { "background-color": "#4CAF50", "color": "white" },
    }

  main_menu = option_menu(
    menu_title='',
    options=menu_options,
    icons=menu_icons,
    default_index=0,
    orientation='horizontal',
    styles=menu_styles,
    #sub_menu={ "Más": ["Subopción 1", "Subopción 2", "Subopción 3"] }
  )

  return main_menu  

# funcion para convertir una imagen de Streamlit en imagenes para PIL y CV2
def parse_image(uploaded_image):
  image = Image.open(uploaded_image)    # convertir a formato PIL
  image_cv2 = np.array(image)            # convertir a array para CV2
  return image, image_cv2

# funcion para obtener los datos de la imagen para el download
def image_data(cv_image):
  _, buffer = cv2.imencode('.jpg', cv_image)
  io_bytes = io.BytesIO(buffer)
  return io_bytes


# variables de sesion
uploaded_image = None

if 'uploaded_image' in st.session_state:
  uploaded_image = st.session_state.uploaded_image


# MENU LATERAL
sidebar_options = ['Inicio', 'Procesar', 'Descargar', 'Acerca de']
sidebar_icons = ['house', 'gear', 'gear']
with st.sidebar:
  sidebar = option_menu('Menú principal', sidebar_options, menu_icon='cast', icons=sidebar_icons, default_index=1)


# PAGINA 'INICIO'
if sidebar == sidebar_options[0]:

  # subir de una imagen
  st.subheader("📷 Sube una imagen para comenzar")
  uploaded_image = st.file_uploader("upload photo", type=["jpg", "png", "gif", "jpeg"], label_visibility='hidden')

  if uploaded_image is not None:
    st.session_state.uploaded_image = uploaded_image  # guardar en sesion
    image, image_np = parse_image(uploaded_image)     # procesar imagen

    # mostrar la imagen original
    st.subheader("Imagen Original")
    container_width = st.checkbox("ajustar a la pantalla", value=True)
    st.image(image, caption="imagen original", use_container_width=container_width)


# PAGINA 'PROCESAR'
if sidebar == 'Procesar':

  # mostrar el menu principal
  main_menu = get_main_menu()

  # opciones  
  if main_menu == 'Grises' and uploaded_image is not None:
    st.subheader("Escala de Grises")

    # aplicar escala de grises
    image, image_cv2 = parse_image(uploaded_image)
    processed_image = cv2.cvtColor(image_cv2, cv2.COLOR_RGB2GRAY)

    # vista previa + download
    st.image(processed_image, caption="imagen en escala de grises", channels="GRAY", use_container_width=True)
    # st.download_button(label="Descargar imagen", data=image_data(processed_image), file_name="processed_image.jpg", mime="image/jpg")

  if main_menu == 'Suavizado Blur' and uploaded_image is not None:
    st.subheader("Suavizado")

    col1, col2 = st.columns(2)            # sliders para ajustar parámetros
    with col1:  ksize = st.slider("Tamaño de Kernel", min_value=1, max_value=25, value=7, step=2) 
    with col2:  sigmaX = st.slider("SigmaX", min_value=0, max_value=10, value=0, step=1) 

    # aplicar suavizado
    image, image_cv2 = parse_image(uploaded_image)
    processed_image = cv2.GaussianBlur(image_cv2, ksize=(ksize, ksize), sigmaX=sigmaX)

    # vista previa & download
    st.image(processed_image, caption="imagen suavizada", use_container_width=True)
    # st.download_button(label="Descargar imagen", data=image_data(processed_image), file_name="processed_image.jpg", mime="image/jpg")

  if main_menu == 'Bordes Canny' and uploaded_image is not None:
    st.subheader("Detección de Bordes (Canny)")

    # slider para ajustar parámetros
    col1, col2 = st.columns(2)
    with col1:  threshold1 = st.slider("Umbral 1 (borde débil)", min_value=0, max_value=255, value=100, step=1)
    with col2:  threshold2 = st.slider("Umbral 2 (borde fuerte)", min_value=0, max_value=255, value=200, step=1)

    # aplicar escala de grises y luego detectar bordes
    image, image_cv2 = parse_image(uploaded_image)
    gray_image = cv2.cvtColor(image_cv2, cv2.COLOR_RGB2GRAY)
    processed_image = cv2.Canny(gray_image, threshold1=threshold1, threshold2=threshold2)

    # vista previa & download
    st.image(processed_image, caption="bordes detectados", use_container_width=True)
    # st.download_button(label="Descargar imagen", data=image_data(processed_image), file_name="processed_image.jpg", mime="image/jpg")


# PAGINA 'ACERCA DE'
if sidebar == 'Acerca de':
  st.subheader('ISSD / Proc. de Imágenes / Parcial 01')
  st.write('')
  st.write('Por: Andres Garcia Alves')
  st.write('Profesor: Lucas de Rito')
