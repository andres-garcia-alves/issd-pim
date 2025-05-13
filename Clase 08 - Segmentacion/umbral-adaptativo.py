import numpy as np
import cv2
import streamlit as st

st.title("Umbralización Adaptativa")

uploaded_file = st.file_uploader("Sube una imagen en formato JPG o PNG", type=["jpg", "png"])

if uploaded_file:
  file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
  image = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)

  st.image(image, caption="Imagen Original", use_container_width=True, channels="GRAY" )

  # aplicar la Umbralización Adaptativa (Media)
  adaptive_thresh_mean = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

  # aplicar Umbralización Adaptativa (Gaussiana)
  adaptive_thresh_gauss = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

  # mostrar resultados
  st.image(adaptive_thresh_mean, caption="Umbralización Adaptativa (Media)", use_container_width=True, channels="GRAY")
  st.image(adaptive_thresh_gauss, caption="Umbralización Adaptativa (Gaussiana)", use_container_width=True, channels="GRAY")
