import streamlit as st
import numpy as np
import cv2  # pip install opencv-python
from PIL import Image

st.title("Aplicación de Filtros Básicos de Imágenes")

# subida de imagen
uploaded_file = st.file_uploader("Sube una imagen", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:

  # convertir la imagen cargada a un formato compatible
  image = Image.open(uploaded_file)
  image_np = np.array(image)

  # mostrar la imagen original
  st.subheader("Imagen Original")
  st.image(image, caption="Imagen Original", use_container_width=True)
 
  # seleccionar el filtro a aplicar
  filtro = st.selectbox("Selecciona un filtro:", ["Escala de grises", "Suavizado (Blur)", "Detección de bordes (Canny)"])

  # procesar la imagen según el filtro seleccionado
  if filtro == "Escala de grises":
    st.subheader("Imagen en Escala de Grises")

    # convertir a escala de grises
    processed_image = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)
    st.image(processed_image, caption="Imagen en escala de grises", channels="GRAY", use_container_width=True)

  elif filtro == "Suavizado (Blur)":
    st.subheader("Imagen suavizada")

    # aplicar suavizado
    processed_image = cv2.GaussianBlur(image_np, (15, 15), 0)
    st.image(processed_image, caption="Imagen Suavizada", use_container_width=True)

  elif filtro == "Detección de bordes (Canny)":
    st.subheader("Bordes Detectados")

    # convertir a escala de grises & detectar bordes
    gray_image = cv2.cvtColor(image_np, cv2.COLOR_RGB2GRAY)
    processed_image = cv2.Canny(gray_image, 100, 200)
    st.image(processed_image, caption="Bordes detectados", use_container_width=True)

  else:
    st.write("Por favor, sube una imagen para comenzar.")
