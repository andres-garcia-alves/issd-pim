import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import cv2
from PIL import Image

st.title("Ecualización de Histograma")

imagen_subida = st.file_uploader("Sube una imagen (JPG/PNG)", type=["jpg", "jpeg", "png"])

if imagen_subida is not None:

  # convertir la imagen a escala de grises
  imagen_pil = Image.open(imagen_subida).convert("L") # Pillow
  imagen = np.array(imagen_pil)                       # NumPy

  # aplicar ecualización del histograma
  imagen_ecualizada = cv2.equalizeHist(imagen)

  # mostrar las imágenes lado a lado
  st.write("### Comparación de Imágenes")
  col1, col2 = st.columns(2)
  with col1:  st.image(imagen, caption="Imagen Original", use_container_width=True, clamp=True)
  with col2:  st.image(imagen_ecualizada, caption="Imagen Ecualizada", use_container_width=True, clamp=True)

  # calcular los histogramas
  hist_original = cv2.calcHist([imagen], [0], None, [256], [0, 256])
  hist_ecualizado = cv2.calcHist([imagen_ecualizada], [0], None, [256], [0, 256])

  # graficar los histogramas
  st.write("### Histogramas")

  fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
  ax1.plot(hist_original, color='blue', linewidth=2)
  ax1.set_title("Histograma Original")
  ax1.set_xlabel("Niveles de Intensidad")
  ax1.set_ylabel("Frecuencia")

  ax2.plot(hist_ecualizado, color='green', linewidth=2)
  ax2.set_title("Histograma Ecualizado")
  ax2.set_xlabel("Niveles de Intensidad")
  ax2.set_ylabel("Frecuencia")
  st.pyplot(fig)
