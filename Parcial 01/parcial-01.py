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


# ===========================================================================
# CONFIG. DE PAG. + VARIABLES DE SESION + FUNCIONES AUXILIARES
# ===========================================================================

# config. de la pagina: titulo, icono y formato ancho
st.set_page_config(
  page_title='ISSD | PIM',
  page_icon='https://raw.githubusercontent.com/andres-garcia-alves/issd-pim/refs/heads/main/Parcial%2001/issd-icon.png',
  layout='centered' # posibles valores: centered, wide
)

# variables de sesion
uploaded_image = st.session_state.get('uploaded_image', None)   # valor x default: None

# funcion auxiliar: convertir una imagen de Streamlit en imagenes para PIL y CV2
def parse_image(uploaded_image):
  image = Image.open(uploaded_image)          # convertir a formato PIL
  image_cv2 = np.array(image)                 # convertir a array para CV2
  return image, image_cv2

# funcion auxiliar: obtener un buffer de la imagen para su descarga
def get_image_data(image_cv2):
  _, buffer = cv2.imencode('.jpg', image_cv2) # codificar a JPG
  io_bytes = io.BytesIO(buffer)               # buffer en memoria (stream)
  return io_bytes


# ===========================================================================
# CONSTRUIR y MOSTRAR SUB-CONTENIDOS DE LAS PAGINAS
# ===========================================================================

# construir un preview de la imagen y un boton de download
def build_preview_download(processed_image, caption):
  if processed_image is not None:
    st.image(processed_image, caption=caption, use_container_width=True)
    st.download_button(label='⬇️ Descargar imagen', data=get_image_data(processed_image), file_name='imagen.jpg', mime='image/jpg')

# construir el contenido para la 'barra de herramientas'
def build_toolbar_menu_content():
  menu_options = ['Escalado', 'Rotación', 'Traslación', 'Escala de Grises', 'Suavizado', 'Detectar Bordes']
  menu_icons = ['arrows-fullscreen', 'arrow-counterclockwise', 'arrows-move', 'back', 'moon', 'arrow-down-right-square']
  menu_styles = {
    'icon': { 'color': 'white', 'font-size': '24px' },
    'nav-link': { 'font-size': '16px', 'text-align': 'center', 'margin': '0px', 'min-width': '100px' },
    'nav-link-selected': { 'background-color': '#4CAF50', 'color': 'white' }
  }

  main_menu = option_menu('Editor de Imágenes', menu_icon='cast', options=menu_options, icons=menu_icons, styles=menu_styles, orientation='horizontal')
  return main_menu  

# construir el contenido para 'escala de grises'
def build_gray_scale_content(uploaded_image):
  st.subheader("Escala de Grises")

  # aplicar escala de grises
  image, image_cv2 = parse_image(uploaded_image)
  processed_image = cv2.cvtColor(image_cv2, cv2.COLOR_RGB2GRAY)
  build_preview_download(processed_image, 'imagen en escala de grises')

# construir el contenido para 'suavizado'
def build_smoothing_content(uploaded_image):
  st.subheader("Suavizado")
  sub_menu = st.selectbox('Método', ['Blur', 'Gaussiano'])

  if sub_menu == 'Blur':
    st.write('blur ...')

  if sub_menu == 'Gaussiano':
    col1, col2 = st.columns(2)                # sliders para ajustar parámetros
    with col1:  ksize = st.slider('Tamaño de Kernel', min_value=1, max_value=25, value=7, step=2) 
    with col2:  sigmaX = st.slider('Sigma X', min_value=0, max_value=10, value=0, step=1) 

    # aplicar suavizado
    image, image_cv2 = parse_image(uploaded_image)
    processed_image = cv2.GaussianBlur(image_cv2, ksize=(ksize, ksize), sigmaX=sigmaX)
    build_preview_download(processed_image, 'imagen suavizada')

# construir el contenido para 'detección de bordes'
def build_edge_detection_content(uploaded_image):
  processed_image = None
  st.subheader('Detección de Bordes')
  sub_menu = st.selectbox('Método', ['Canny', 'Sobel'])

  if sub_menu == 'Canny':
    col1, col2 = st.columns(2)              # sliders para ajustar parámetros
    with col1:  threshold1 = st.slider("Umbral 1 (borde débil)", min_value=0, max_value=255, value=100, step=1)
    with col2:  threshold2 = st.slider("Umbral 2 (borde fuerte)", min_value=0, max_value=255, value=200, step=1)

    # aplicar escala de grises y luego detectar bordes
    image, image_cv2 = parse_image(uploaded_image)
    gray_image = cv2.cvtColor(image_cv2, cv2.COLOR_RGB2GRAY)
    processed_image = cv2.Canny(gray_image, threshold1=threshold1, threshold2=threshold2)
    build_preview_download(processed_image, 'bordes detectados')

  if sub_menu == 'Sobel':
    st.write('sobel ...')
    # col1, col2 = st.columns(2)            # sliders para ajustar parámetros
    # with col1:  threshold1 = st.slider("Umbral 1 (borde débil)", min_value=0, max_value=255, value=100, step=1)
    # with col2:  threshold2 = st.slider("Umbral 2 (borde fuerte)", min_value=0, max_value=255, value=200, step=1)

    # # aplicar escala de grises y luego detectar bordes
    # image, image_cv2 = parse_image(uploaded_image)
    # gray_image = cv2.cvtColor(image_cv2, cv2.COLOR_RGB2GRAY)
    # processed_image = cv2.Canny(gray_image, threshold1=threshold1, threshold2=threshold2)

    # # vista previa
    # st.image(processed_image, caption="bordes detectados", use_container_width=True)


# ===========================================================================
#  MENU LATERAL
# ===========================================================================
sidebar_options = ['Inicio', 'Procesar', 'Acerca de']
sidebar_icons = ['house', 'gear', 'info-circle']
sidebar_styles = {
  'nav-link-selected': { 'background-color': '#4CAF50', 'color': 'white', 'font-weight': 'normal' }
}
with st.sidebar:
  sidebar = option_menu('Menú Principal', sidebar_options, menu_icon='cast', icons=sidebar_icons, styles=sidebar_styles, default_index=0)


# ===========================================================================
# PAGINA 'INICIO'
# ===========================================================================
if sidebar == 'Inicio':

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


# ===========================================================================
# PAGINA 'PROCESAR'
# ===========================================================================
if sidebar == 'Procesar':
  
  main_menu = build_toolbar_menu_content()    # mostrar la barra de herramientas

  if main_menu == 'Escala de Grises' and uploaded_image is not None:
    build_gray_scale_content(uploaded_image)

  if main_menu == 'Suavizado' and uploaded_image is not None:
    build_smoothing_content(uploaded_image)

  if main_menu == 'Detectar Bordes' and uploaded_image is not None:
    build_edge_detection_content(uploaded_image)


# ===========================================================================
# PAGINA 'ACERCA DE'
# ===========================================================================
if sidebar == 'Acerca de':

  logo_url = 'https://raw.githubusercontent.com/andres-garcia-alves/issd-pim/refs/heads/main/Parcial%2001/issd-logo.png'
  st.image(logo_url, caption='', use_container_width=False)

  st.subheader('ISSD / Proc. de Imágenes / Parcial 01')
  st.write('')
  st.write('Por: Andres Garcia Alves')
  st.write('Profesor: Lucas de Rito')
