import numpy as np
import cv2
import streamlit as st

st.title("Umbralización Global")

uploaded_file = st.file_uploader("Sube una imagen en formato JPG o PNG", type=["jpg", "png"])

if uploaded_file:
  file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
  image = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)

  st.image(image, caption="Imagen Original", use_container_width=True, channels="GRAY")

  threshold_value = 127   # umbral fijo
  max_value = 255         # valor asignado a píxeles superiores al umbral

  # aplicar la Umbralización Global
  _, binary_image = cv2.threshold(image, threshold_value, max_value, cv2.THRESH_BINARY)

  st.image(binary_image, caption="Imagen Umbralizada", use_container_width=True, channels="GRAY")
