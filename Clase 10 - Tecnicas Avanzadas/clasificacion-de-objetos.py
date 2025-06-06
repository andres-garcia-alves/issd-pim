import numpy as np
import cv2
from PIL import Image
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
import streamlit as st

# cargar el modelo preentrenado MobileNetV2 de ImageNet
model = MobileNetV2(weights='imagenet')

st.title("Clasificación de Imagen con MobileNetV2")

uploaded_file = st.file_uploader("Sube una imagen", type=["jpg", "jpeg", "png","webp"])

if uploaded_file is not None:

  image = Image.open(uploaded_file)
  st.image(image, caption='Imagen cargada', use_container_width=True)

  # boton para detectar/clasificar
  if st.button("Detectar objeto"):

    # convertir la imagen de PIL a un array de NumPy
    image_array = np.array(image)

    # ajustar la imagen al tamaño que requiere MobileNetV2 (224x224)
    resized_img = cv2.resize(image_array, (224, 224))

    # convertir a float32 (para evitar posibles problemas de tipo)
    resized_img = resized_img.astype(np.float32)

    # expandir dimensión para que sea (1, 224, 224, 3)
    img_batch = np.expand_dims(resized_img, axis=0)

    # normalizamos los valores con la función de MobileNetV2
    img_batch = preprocess_input(img_batch)

    # realizar la predicción
    predictions = model.predict(img_batch)
    decoded = decode_predictions(predictions, top=3)[0]

    # mostrar los resultados
    st.subheader("Predicciones:")
    for i, (imagenet_id, label, score) in enumerate(decoded):
      st.write(f"{ i + 1 }. **{ label }** - Confianza: { round(score, 2) }")

    st.success("¡Clasificación completada!")
