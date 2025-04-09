import streamlit as st
import numpy as np
import io
import cv2  # pip install opencv-python
from PIL import Image

# funcion para obtener los datos de la imagen
def image_data(cv_image):
  _, buffer = cv2.imencode('.jpg', cv_image)
  io_bytes = io.BytesIO(buffer)
  return io_bytes


# titulo
st.title("Filtros Básicos de Imágenes")

# subida de imagen
uploaded_file = st.file_uploader("Sube una imagen", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:

  # convertir la imagen cargada a un formato compatible
  image = Image.open(uploaded_file)
  image_np = np.array(image)

  # mostrar la imagen original
  st.subheader("Imagen Original")
  container_width = st.checkbox("ajustar tamaño", value=True)
  asd = st.image(image, caption="Imagen Original", use_container_width=container_width)
 
  # seleccionar el filtro
  st.write("")
  filtro = st.selectbox("Selecciona un filtro:", ["---", "Escala de grises", "Suavizado (Blur)", "Detección de bordes (Canny)"])

  # escala de grises
  if filtro == "Escala de grises":
    st.subheader("Imagen en Escala de Grises")

    # aplicar escala de grises
    processed_image = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)

    # vista previa & download
    st.image(processed_image, caption="Imagen en escala de grises", channels="GRAY", use_container_width=container_width)
    st.download_button(label="Descargar imagen", data=image_data(processed_image), file_name="processed_image.jpg", mime="image/jpg")

  # suavizado
  elif filtro == "Suavizado (Blur)":
    st.subheader("Imagen suavizada")

    # slider para ajustar parámetros
    col1, col2 = st.columns(2)
    with col1:
      ksize = st.slider("Propiedad **KSize**:", min_value=1, max_value=25, value=7, step=2) 
    with col2:
      sigmaX = st.slider("Propiedad **SigmaX**:", min_value=0, max_value=10, value=0, step=1) 

    # aplicar suavizado
    processed_image = cv2.GaussianBlur(image_np, ksize=(ksize, ksize), sigmaX=sigmaX)

    # vista previa & download
    st.image(processed_image, caption="Imagen Suavizada", use_container_width=container_width)
    st.download_button(label="Descargar imagen", data=image_data(processed_image), file_name="processed_image.jpg", mime="image/jpg")

  # detección de bordes
  elif filtro == "Detección de bordes (Canny)":
    st.subheader("Bordes Detectados")

    # slider para ajustar parámetros
    col1, col2 = st.columns(2)
    with col1:
      threshold1 = st.slider("Propiedad **Threshold1** (borde débil):", min_value=0, max_value=255, value=100, step=1)
    with col2:
      threshold2 = st.slider("Propiedad **Threshold2** (borde fuerte):", min_value=0, max_value=255, value=200, step=1)

    # aplicar escala de grises y luego detectar bordes
    gray_image = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)
    processed_image = cv2.Canny(gray_image, threshold1=threshold1, threshold2=threshold2)

    # vista previa & download
    st.image(processed_image, caption="Bordes detectados", use_container_width=container_width)
    st.download_button(label="Descargar imagen", data=image_data(processed_image), file_name="processed_image.jpg", mime="image/jpg")

  else:
    st.write("Por favor, sube una imagen y selecciona un filtro.")
