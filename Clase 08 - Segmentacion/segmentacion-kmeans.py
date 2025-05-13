import numpy as np
import cv2
import streamlit as st

st.title("Segmentación con K-means")
uploaded_file = st.file_uploader("Sube una imagen en formato JPG o PNG", type=["jpg", "png"])

if uploaded_file:
  file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
  image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

  st.image(image, caption="Imagen Original", use_container_width=True, channels="BGR")

  # convertir la imagen a un formato adecuado para K-means
  # cada fila representa un píxel y sus valores RGB
  data = image.reshape((-1, 3))
  data = np.float32(data)

  # parámetros para el algoritmo K-means
  k = st.slider("Número de Clústeres (k)", min_value=2, max_value=10, value=3)
  criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

  # aplicar el algoritmo K-means
  _, labels, centers = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
  # print('Etiquetas:', '\n', labels, '\n')
  # print('Centros:', '\n', centers, '\n')

  # convertir los centros a valores enteros
  centers = np.uint8(centers)
  segmented_image = centers[labels.flatten()]
  segmented_image = segmented_image.reshape(image.shape)

  # mostrar la imagen segmentada
  st.image(segmented_image, caption="Imagen Segmentada con K-means", use_container_width=True, channels="BGR")
