import numpy as np
import cv2
import streamlit as st

np.set_printoptions(linewidth=200)   # saltos de línea (otra opción: linewidth=np.inf) 130
np.set_printoptions(edgeitems=24)    # mostrar más elementos al principio y final
np.set_printoptions(threshold=260)   # ancho para los arrays

st.title("Segmentación con Watershed")

uploaded_file = st.file_uploader("Sube una imagen en formato JPG o PNG", type=["jpg", "png"])
container_width = st.checkbox("Ajustar imagen al tamaño disponible", value=True)

if uploaded_file:

  file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
  image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
  image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # aplicar desenfoque para reducir el ruido
  image_blur = cv2.GaussianBlur(image_gray, (5, 5), 0)

  # aplicar la detección de bordes
  edges = cv2.Canny(image_blur, 50, 150)

  # generar una imagen binaria para los marcadores
  _, binary = cv2.threshold(edges, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

  # aplicar distancia euclidiana para detectar regiones
  distance_transform = cv2.distanceTransform(binary, cv2.DIST_L2, 5)
  thresh = 0.7 * distance_transform.max()
  _, area_foreground = cv2.threshold(distance_transform, thresh, 255, 0)

  # detectar las regiones desconocidas (fondo)
  area_foreground = np.uint8(area_foreground)
  area_background = cv2.subtract(binary, area_foreground)
  print('Región desconocida:', '\n', area_background, '\n')

  # etiquetar las regiones iniciales (marcadores)
  _, markers = cv2.connectedComponents(area_foreground)
  print('Markers (paso 1):', '\n', markers, '\n')

  markers = markers + 1
  print('Markers (paso 2):', '\n', markers, '\n')

  # las regiones desconocidas se etiquetan como 0 para diferenciarlas
  markers[area_background == 255] = 0
  print('Markers (paso 3):', '\n', markers, '\n')

  # aplicar el algoritmo Watershed
  markers = cv2.watershed(image, markers)
  print('Markers (paso 4):', '\n', markers, '\n')

  # marcar los bordes de las regiones en rojo
  image_processed = image.copy()
  image_processed[markers == -1] = [0, 0, 255]

  # mostrar la imagen original y la imagen segmentada
  st.image(image, caption="Imagen Original", use_container_width=container_width, channels="BGR")
  st.image(image_processed, caption="Imagen Segmentada (Watershed)", use_container_width=container_width, channels="BGR")
