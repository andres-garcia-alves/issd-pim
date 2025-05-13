import numpy as np
import cv2
import streamlit as st

st.title("Identificación y Etiquetado de Objetos en Imágenes")
uploaded_file = st.file_uploader("Sube una imagen en formato JPG, PNG o WEBP", type=["jpg", "png", "webp"])

if uploaded_file:
  file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
  image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

  st.image(image, caption="Imagen Original", use_container_width=True, channels="BGR")
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # aplicar suavizado para reducir ruido
  blurred = cv2.GaussianBlur(gray, (5, 5), 0)

  # segmentación Binaria
  _, binary = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV)

  # limpiar la imagen binaria con operaciones morfológicas
  kernel = np.ones((5, 5), np.uint8)
  binary_cleaned = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
  binary_cleaned = cv2.dilate(binary_cleaned, kernel, iterations=1)

  # mostrar la imagen binarizada limpia
  st.image(binary_cleaned, caption="Imagen Binarizada y Limpia", use_container_width=True, channels="GRAY")

  # identificación de Componentes Conectados
  num_labels, labels = cv2.connectedComponents(binary_cleaned)

  # asignar colores aleatorios a cada etiqueta
  label_colors = np.random.randint(0, 255, size=(num_labels, 3), dtype=np.uint8)
  labeled_image = np.zeros_like(image)

  for label in range(1, num_labels):  # saltar el fondo
    labeled_image[labels == label] = label_colors[label]

  # mostrar la imagen etiquetada
  st.image(labeled_image, caption="Imagen Etiquetada", use_container_width=True, channels="BGR")

  # detectar contornos de los objetos
  contours, _ = cv2.findContours(binary_cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  # filtrar contornos válidos por area minima
  valid_contours = []
  min_contour_area = 500  # area minima para considerar un contorno como valido

  for contour in contours:
    if cv2.contourArea(contour) >= min_contour_area:
      valid_contours.append(contour)

  # dibujar bounding-boxes
  boxed_image = image.copy()
  for contour in valid_contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(boxed_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

  # mostrar la imagen con Bounding Boxes
  st.image(boxed_image, caption="Bounding Boxes Dibujados", use_container_width=True, channels="BGR")

  # mostrar el número final de objetos detectados
  st.write(f"Número total de objetos detectados: { len(valid_contours) }")
