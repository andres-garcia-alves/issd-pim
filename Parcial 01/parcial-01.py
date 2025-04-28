import io
import numpy as np
import cv2
from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu


# ===========================================================================
# CONFIG. DE PAG. + VARIABLES DE SESION + FUNCIONES AUXILIARES
# ===========================================================================

# config. de la pagina: titulo, icono y formato ancho
st.set_page_config(
  page_title='ISSD | PIM',
  page_icon='https://raw.githubusercontent.com/andres-garcia-alves/issd-pim/refs/heads/main/Parcial%2001/issd-icon.png',
  layout='centered' # posibles valores: centered, wide
)

# variable de sesion
uploaded_image = st.session_state.get('uploaded_image', None) # valor x default: None

# funcion auxiliar: convertir una imagen de Streamlit en imagenes para PIL y CV2
def parse_image(uploaded_image):
  image = Image.open(uploaded_image)            # convertir a formato PIL
  image_cv2 = np.array(image)                   # convertir a array para CV2
  return image, image_cv2

# funcion auxiliar: obtener un buffer de la imagen para su descarga
def get_image_data(image_cv2):
  image_rgb = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2RGB)  # covertir BGR a RGB
  _, buffer = cv2.imencode('.jpg', image_rgb)   # codificar a JPG
  return io.BytesIO(buffer)                     # retornar el buffer en memoria (stream)


# ===========================================================================
# CONSTRUIR y MOSTRAR SUB-CONTENIDOS DE LAS PAGINAS
# ===========================================================================

# construir un preview de la imagen y un boton de download
def build_preview_download(processed_image, caption, use_container_width=True, checkbox_container_width=False):
  if processed_image is not None:
    if checkbox_container_width:
      use_container_width = st.checkbox('ajustar a la pantalla', value=use_container_width)

    st.image(processed_image, caption=caption, use_container_width=use_container_width)
    st.download_button(label='⬇️ Descargar Imagen', data=get_image_data(processed_image), file_name='imagen.jpg', mime='image/jpg')

# construir el contenido para la 'barra de herramientas'
def build_toolbar_menu_content():
  menu_options = ['Escalado', 'Rotación', 'Traslación', 'Escala de Grises', 'Suavizado', 'Detección de Bordes']
  menu_icons   = ['arrows-fullscreen', 'arrow-counterclockwise', 'arrows-move', 'back', 'moon', 'arrow-down-right-square']
  menu_styles  = {
    'icon': { 'color': 'white', 'font-size': '24px' },
    'nav-link': { 'font-size': '16px', 'text-align': 'center', 'margin': '0px', 'min-width': '100px' },
    'nav-link-selected': { 'background-color': '#4CAF50', 'color': 'white' }
  }

  main_menu = option_menu('Herramientas', options=menu_options, menu_icon='gear', icons=menu_icons, styles=menu_styles, orientation='horizontal')
  return main_menu  

# construir el contenido para la herramienta 'escalado'
def build_rescale_content(uploaded_image):
  st.subheader('Escalar')

  _, image_cv2 = parse_image(uploaded_image)
  height, width, _ = image_cv2.shape

  # metodo de interpolacion
  interp_dic = { 'Cercanía': cv2.INTER_NEAREST, 'Lineal': cv2.INTER_LINEAR, 'Cúbica': cv2.INTER_CUBIC, 'Lanczos': cv2.INTER_LANCZOS4 }
  interp_key = st.radio('Método de Interpolación', interp_dic.keys(), horizontal=True)
  interp_value = interp_dic[interp_key] # buscar el 'value' para la 'key' seleccionada

  # ajustar por porcentajes vs especificar pixels
  adjustment = st.radio('Ajustar', ['Porcentaje', 'Pixels'], horizontal=True)

  if adjustment == 'Porcentaje':
    col1, col2 = st.columns(2) # sliders para ajustar parámetros
    with col1:  factor_x = st.slider('Ancho (%)', value=100, min_value=5, max_value=500, step=5)
    with col2:  factor_y = st.slider('Alto (%)', value=100, min_value=5, max_value=500, step=5)
    processed_image = cv2.resize(image_cv2, None, fx=factor_x/100, fy=factor_y/100, interpolation=interp_value)

  else:
    col1, col2 = st.columns(2) # sliders para ajustar parámetros
    with col1:  pixels_x = st.slider('Ancho (pixels)', value=width, min_value=1, max_value=height*5, step=1)
    with col2:  pixels_y = st.slider('Alto (pixels)', value=height, min_value=1, max_value=width*5, step=1)
    processed_image = cv2.resize(image_cv2, dsize=(pixels_x, pixels_y), interpolation=interp_value)

  # escalar imagen
  build_preview_download(processed_image, 'imagen re-escalada', True, True)

# construir el contenido para la herramienta 'rotacion'
def build_rotate_content(uploaded_image):
  st.subheader('Rotar')

  col1, col2 = st.columns(2) # sliders para ajustar parámetros
  with col1:  angle = st.slider('Angulo', value=45, min_value=0, max_value=360, step=5)
  with col2:  scale = st.slider('Escala (tamaño original: 1.00)', value=1.0, min_value=0.1, max_value=2.0, step=0.1)

  # rotar imagen
  _, image_cv2 = parse_image(uploaded_image)
  height, width, _ = image_cv2.shape
  center = (width // 2, height // 2)

  # crear la matriz de rotacion y aplicar la transformacion
  M = cv2.getRotationMatrix2D(center, angle, scale)
  processed_image = cv2.warpAffine(image_cv2, M, (width, height))
  build_preview_download(processed_image, 'imagen rotada', True, True)

# construir el contenido para la herramienta 'traslacion'
def build_traslation_content(uploaded_image):
  st.subheader('Trasladar')

  _, image_cv2 = parse_image(uploaded_image)
  height, width, _ = image_cv2.shape
  #height, 

  col1, col2 = st.columns(2) # sliders para ajustar parámetros
  with col1:  x_axis = st.slider('Eje X', value=0, min_value=-width, max_value=width, step=1)
  with col2:  y_axis = st.slider('Eje Y', value=0, min_value=-height, max_value=height, step=1)

  # trasladar imagen
  M = np.float32([ [1, 0, x_axis], [0, 1, y_axis] ])
  processed_image = cv2.warpAffine(image_cv2, M, (y_axis, x_axis))
  build_preview_download(processed_image, 'imagen trasladada')

# construir el contenido para la herramienta 'escala de grises'
def build_gray_scale_content(uploaded_image):
  st.subheader("Escala de Grises")

  # aplicar escala de grises
  _, image_cv2 = parse_image(uploaded_image)
  processed_image = cv2.cvtColor(image_cv2, cv2.COLOR_RGB2GRAY)
  build_preview_download(processed_image, 'imagen en escala de grises')

# construir el contenido para la herramienta 'suavizado'
def build_smoothing_content(uploaded_image):
  st.subheader('Suavizar')
  sub_menu = st.selectbox('Método', ['Blur', 'Gaussiano'])

  if sub_menu == 'Blur':
    kernel = st.slider('Tamaño de Kernel', value=1, min_value=1, max_value=25, step=1)

    # aplicar suavizado
    _, image_cv2 = parse_image(uploaded_image)
    processed_image = cv2.blur(image_cv2, ksize=(kernel, kernel))
    build_preview_download(processed_image, 'imagen suavizada')

  if sub_menu == 'Gaussiano':
    col1, col2 = st.columns(2) # sliders para ajustar parámetros
    with col1:  ksize = st.slider('Tamaño de Kernel', value=7, min_value=1, max_value=25, step=2) 
    with col2:  sigmaX = st.slider('Sigma X', value=0, min_value=0, max_value=10, step=1) 

    # aplicar suavizado
    _, image_cv2 = parse_image(uploaded_image)
    processed_image = cv2.GaussianBlur(image_cv2, ksize=(ksize, ksize), sigmaX=sigmaX)
    build_preview_download(processed_image, 'imagen suavizada')

# construir el contenido para la herramienta 'detección de bordes'
def build_edge_detection_content(uploaded_image):
  processed_image = None
  st.subheader('Detección de Bordes')
  sub_menu = st.selectbox('Método', ['Canny', 'Sobel'])

  if sub_menu == 'Canny':
    col1, col2 = st.columns(2) # sliders para ajustar parámetros
    with col1:  threshold1 = st.slider("Umbral 1 (borde débil)", value=100, min_value=0, max_value=255, step=1)
    with col2:  threshold2 = st.slider("Umbral 2 (borde fuerte)", value=200, min_value=0, max_value=255, step=1)

    # aplicar escala de grises y luego detectar bordes
    _, image_cv2 = parse_image(uploaded_image)
    processed_image = cv2.cvtColor(image_cv2, cv2.COLOR_RGB2GRAY)
    processed_image = cv2.Canny(processed_image, threshold1=threshold1, threshold2=threshold2)
    build_preview_download(processed_image, 'bordes detectados')

  if sub_menu == 'Sobel':
    kernel = st.slider('Tamaño de Kernel', value=1, min_value=1, max_value=25, step=2)

    _, image_cv2 = parse_image(uploaded_image)
    image_cv2 = cv2.cvtColor(image_cv2, cv2.COLOR_RGB2GRAY)         # convertir a escala de grises

    sobel_x = cv2.Sobel(image_cv2, cv2.CV_64F, 1, 0, ksize=kernel)  # bordes horizontales
    sobel_y = cv2.Sobel(image_cv2, cv2.CV_64F, 0, 1, ksize=kernel)  # bordes verticales
    sobel_comb = cv2.magnitude(sobel_x, sobel_y)                    # magnitud combinada de los bordes

    processed_image = cv2.normalize(sobel_comb, None, 0, 255, cv2.NORM_MINMAX) # normalizar a rango 0-255
    processed_image = processed_image.astype(np.uint8)              # covertir de float a byte para st.image()
    build_preview_download(processed_image, 'bordes detectados')


# ===========================================================================
#  MENU LATERAL
# ===========================================================================
sidebar_options = ['Inicio', 'Herramientas', 'Métricas', 'Acerca de']
sidebar_icons   = ['house', 'gear', 'calculator', 'info-circle']
sidebar_styles  = { 'nav-link-selected': { 'background-color': '#4CAF50', 'color': 'white', 'font-weight': 'normal' } }

with st.sidebar:
  sidebar = option_menu('Menú Principal', sidebar_options, menu_icon='cast', icons=sidebar_icons, default_index=0, styles=sidebar_styles)

# ===========================================================================
# PAGINA 'INICIO'
# ===========================================================================
if sidebar == 'Inicio':

  # subir de una imagen
  st.subheader('📷 Sube una imagen para comenzar')
  st.text("👉🏻 Luego selecciona '⚙️ Herramientas' del menú lateral cuando estés listo para continuar.")
  uploaded_image = st.file_uploader("upload photo", type=['jpg', 'png', 'gif', 'jpeg'], label_visibility='hidden')

  if uploaded_image is not None:
    
    st.session_state.uploaded_image = uploaded_image  # guardar en sesion
    image, image_np = parse_image(uploaded_image)     # procesar imagen

    # mostrar la imagen original
    st.subheader('Imagen Original')
    container_width = st.checkbox('ajustar a la pantalla', value=True)
    st.image(image, caption='imagen original', use_container_width=container_width)


# ===========================================================================
# PAGINA 'HERRAMIENTAS'
# ===========================================================================
if sidebar == 'Herramientas':

  main_menu = build_toolbar_menu_content()  # mostrar la barra de herramientas

  if main_menu == 'Escalado' and uploaded_image is not None:
    build_rescale_content(uploaded_image)

  if main_menu == 'Rotación' and uploaded_image is not None:
    build_rotate_content(uploaded_image)

  if main_menu == 'Traslación' and uploaded_image is not None:
    build_traslation_content(uploaded_image)

  if main_menu == 'Escala de Grises' and uploaded_image is not None:
    build_gray_scale_content(uploaded_image)

  if main_menu == 'Suavizado' and uploaded_image is not None:
    build_smoothing_content(uploaded_image)

  if main_menu == 'Detección de Bordes' and uploaded_image is not None:
    build_edge_detection_content(uploaded_image)


# ===========================================================================
# PAGINA 'ESTADISTICAS' (histograma, etc)
# ===========================================================================
if sidebar == 'Métricas':
  st.write('Métricas de la imagen: histograma, etc ...')

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
