import numpy as np
import cv2
from PIL import Image
import streamlit as st

def main():
  st.title("Operaciones Morfológicas en Imágenes")
  st.sidebar.title("Configuración")
  st.write("Carga una imagen y selecciona una operación morfológica para ver el resultado.")

  uploaded_file = st.file_uploader("Sube una imagen", type=["jpg", "jpeg", "png"])

  if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image = np.array(image)

    # convertir a escala de grises si es necesario
    if len(image.shape) == 3:
      image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
      st.image(image, caption="Imagen Original", use_container_width=True, channels="GRAY")

    # selección de operación morfológica en el menú lateral
    operation = st.sidebar.selectbox("Selecciona una operación morfológica", ["Erosión", "Dilatación", "Apertura", "Cierre"])

    # tamaño del elemento estructurante
    kernel_size = st.sidebar.slider("Tamaño del Elemento Estructurante (EE)", 1, 20, 3)
    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    # aplicar la operación seleccionada
    if operation == "Erosión":
      processed_image = cv2.erode(image, kernel, iterations=1)
    elif operation == "Dilatación":
      processed_image = cv2.dilate(image, kernel, iterations=1)
    elif operation == "Apertura":
      processed_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    elif operation == "Cierre":
      processed_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

    # mostrar el resultado
    st.image(processed_image, caption=f"Imagen Procesada - { operation }", use_container_width=True, channels="GRAY")

if __name__ == "__main__":
  main()
