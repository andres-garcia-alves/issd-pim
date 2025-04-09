import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

data = { "Nombre": ["Ana", "Luis", "Carlos"], "Edad": [23, 30, 35] }
df = pd.DataFrame(data)

# cabeceras
st.title("Hola mundo en Streamlit.io")
st.header("Un Header")
st.subheader("Un Sub-header")
st.text("Un texto simple.")
st.markdown("Un ejemplo de markdown: **negritas** y *cursivas*.")
st.write("Una descripcion de prueba con st.write()")

# visualizacion automatica
st.subheader("Visualizacion automática")
st.write(df)

# visualizacion con st.dataframe()
st.subheader("Visualizacion con st.dataframe()")
st.dataframe(df, width=500, height=300)

# visualizacion con st.table()
st.subheader("Visualizacion con st.table()")
st.table(df)

# subir archivos
st.subheader("Subir archivos")
uploaded_file = st.file_uploader("Sube un archivo", type=['txt', 'csv', 'jpg', 'png'])
if uploaded_file is not None:
    st.write("Archivo subido", uploaded_file.name)
else:
    st.write("Por favor, sube un archivo.")

# imagenes
st.subheader("Imagenes")
image = Image.open("recursos/goku.jpg")
st.image(image, caption="Goku") # use_container_width=True

# widgets
st.subheader("Widgets")
if st.button("Presiona este botón"):
    st.write("Presionado!")

nombre = st.text_input("Ingresa tu nombre:")
if nombre:
    st.write(f"Hola, { nombre }!")

edad = st.number_input("Ingresa tu edad:", min_value=1, max_value=100, step=1)
st.write(f"tienes { edad } años.")

color = st.radio("Tu Color favorito:", ["Rojo", "Verde", "Azul"])
st.write(f"color favorito { color }.")

# st.text_area(), st.slider(), st.checkbox(), st.selectbox()

# graficos: matplotlib, ploty
st.subheader("Gráficos (matplotlib, ploty)")
x = np.linspace(0, 10, 100)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y, label="Seno(x)")
ax.legend()
st.pyplot(fig)

# multimedia
st.subheader("Multimedia")
st.text("audio:")
st.audio("recursos/las pelotas - sera.mp3")
st.text("video:")
st.video("https://www.youtube.com/watch?v=SUMyyx7FCxQ")

# menu lateral
st.subheader("Menu lateral")
st.sidebar.title("barra lateral")
opcion = st.sidebar.selectbox("Opciones:", ["opción #1", "opción #2"])
st.write(f"Elegiste la '{ opcion }' del menu lateral.")

# columnas
st.subheader("Columnas")
col1, col2 = st.columns(2)
col1.write("Columna 1")
col2.write("Columna 2")

# expander
st.subheader("Expander")
with st.expander("Más información"):
    st.write("la descripción detallada va aquí ...")
