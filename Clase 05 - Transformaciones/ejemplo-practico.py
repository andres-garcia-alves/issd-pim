import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Título principal de la aplicación
st.title("Aplicación de Filtros en Imágenes")

# Barra lateral con el menú de opciones
st.sidebar.header("Selecciona un filtro")
filtro = st.sidebar.selectbox("Filtros disponibles", ["Blur (Promedio)", "Gaussian Blur", "Sobel", "Canny"])

# Subir imagen
uploaded_file = st.file_uploader("Sube una imagen", type=["jpg", "png", "jpeg"])

# Si se subió una imagen, procesarla
if uploaded_file is not None:
    # Convertir la imagen cargada a formato OpenCV
    image = Image.open(uploaded_file) # Abrir imagen con PIL
    image_np = np.array(image) # Convertir a arreglo NumPy
    st.image(image, caption="Imagen Original", use_container_width=True) # Mostrar imagen original

    # Procesar según el filtro seleccionado
    if filtro == "Blur (Promedio)":
        st.sidebar.subheader("Parámetros del Filtro Blur")
        kernel_size = st.sidebar.slider("Tamaño del kernel", 1, 15, 5, step=2) # Tamaño del kernel
        # Aplicar filtro Blur (Promedio)
        blurred_image = cv2.blur(image_np, (kernel_size, kernel_size))
        st.image(blurred_image, caption="Imagen con Filtro Blur", use_container_width=True)
    elif filtro == "Gaussian Blur":
        st.sidebar.subheader("Parámetros del Filtro Gaussian Blur")
        kernel_size = st.sidebar.slider("Tamaño del kernel", 1, 15, 5, step=2) # Tamaño del kernel
        # Aplicar filtro Gaussian Blur
        gaussian_image = cv2.GaussianBlur(image_np, (kernel_size, kernel_size), 0)
        st.image(gaussian_image, caption="Imagen con Filtro Gaussian Blur",
        use_container_width=True)
    elif filtro == "Sobel":
        st.sidebar.subheader("Parámetros del Filtro Sobel")
        sobel_dir = st.sidebar.radio("Dirección", ["Horizontal", "Vertical", "Ambos"]) # Dirección
        del filtro
        # Convertir la imagen a escala de grises para aplicar Sobel
        gray_image = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
        if sobel_dir == "Horizontal":
            sobel_image = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3) # Gradiente horizontal
        elif sobel_dir == "Vertical":
            sobel_image = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3) # Gradiente vertical
        else:
            sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3) # Gradiente horizontal
            sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3) # Gradiente vertical
            sobel_image = cv2.magnitude(sobel_x, sobel_y) # Magnitud combinada
            st.image(sobel_image, caption="Imagen con Filtro Sobel", use_container_width=True, clamp=True)
    elif filtro == "Canny":
        st.sidebar.subheader("Parámetros del Filtro Canny")
        lower_threshold = st.sidebar.slider("Umbral inferior", 0, 255, 100) # Umbral inferior
        upper_threshold = st.sidebar.slider("Umbral superior", 0, 255, 200) # Umbral superior
        # Convertir la imagen a escala de grises para aplicar Canny
        gray_image = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
        # Aplicar filtro Canny
        canny_image = cv2.Canny(gray_image, lower_threshold, upper_threshold)
        st.image(canny_image, caption="Imagen con Filtro Canny", use_container_width=True, channels="GRAY")
