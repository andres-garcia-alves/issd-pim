import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import cv2
from PIL import Image

st.title("Mejora de Contraste")

imagen_subida = st.file_uploader("Sube una imagen (JPG/PNG)", type=["jpg", "jpeg", "png"])

if imagen_subida is not None:

  # convertir la imagen a formato OpenCV
  imagen_pil = Image.open(imagen_subida)
  imagen = np.array(imagen_pil)

  # menú lateral para seleccionar la técnica
  st.sidebar.title("Opciones de Mejora de Contraste")
  opcion = st.sidebar.selectbox("Selecciona una técnica:", ("Ajuste Manual de Brillo y Contraste", "Expansión del Histograma"))

  if opcion == "Ajuste Manual de Brillo y Contraste":
    
    # sliders para ajustar brillo y contraste
    contraste = st.sidebar.slider("Contraste", 0.5, 3.0, 1.0, 0.1)
    brillo = st.sidebar.slider("Brillo", -100, 100, 0, 1)

    # aplicar ajuste de brillo y contraste
    imagen_ajustada = cv2.convertScaleAbs(imagen, alpha=contraste, beta=brillo)

    # mostrar imágenes
    st.write("### Imagen Original")
    st.image(imagen, caption="Imagen Original", use_container_width=True)
    st.write("### Imagen Ajustada")
    st.image(imagen_ajustada, caption="Imagen Ajustada", use_container_width=True)

  elif opcion == "Expansión del Histograma":

    # convertir a escala de grises si no lo está
    if len(imagen.shape) == 3: # Imagen RGB
      imagen = cv2.cvtColor(imagen, cv2.COLOR_RGB2GRAY)

    # calcular mínimo y máximo
    min_val = np.min(imagen)
    max_val = np.max(imagen)

    # aplicar expansión del histograma
    imagen_expandida = cv2.normalize(imagen, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    # mostrar imágenes
    st.write("### Imagen Original")
    st.image(imagen, caption="Imagen Original", use_container_width=True)
    st.write("### Imagen con Histograma Expandido")
    st.image(imagen_expandida, caption="Imagen con Histograma Expandido",
    use_container_width=True)

    # visualizar los histogramas
    hist_original = cv2.calcHist([imagen], [0], None, [256], [0, 256])
    hist_expandido = cv2.calcHist([imagen_expandida], [0], None, [256], [0, 256])

    # graficar los histogramas
    st.write("### Comparación de Histogramas")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(hist_original, color='blue', linewidth=2)
    ax1.set_title("Histograma Original")
    ax1.set_xlabel("Niveles de Intensidad")
    ax1.set_ylabel("Frecuencia")

    ax2.plot(hist_expandido, color='green', linewidth=2)
    ax2.set_title("Histograma Expandido")
    ax2.set_xlabel("Niveles de Intensidad")
    ax2.set_ylabel("Frecuencia")

    st.pyplot(fig)
