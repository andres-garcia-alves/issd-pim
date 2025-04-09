import streamlit as st

st.title("Aplicación Interactiva Básica")
st.write("Bienvenido a esta aplicación interactiva creada con Streamlit. Introduce datos y experimenta con los widgets disponibles.")

nombre = st.text_input("¿Cómo te llamas?", "")
edad = st.number_input("¿Cuántos años tienes?", min_value=0, max_value=120, step=1, value=25)
genero = st.radio("Selecciona tu género:", ["Masculino", "Femenino", "Otro"])
nivel_satisfaccion = st.slider("¿Qué tan satisfecho estás con esta aplicación? (0-100)", 0, 100, 50)

if st.button("Enviar"): # el 'if' equivale a un click ¿?
  if nombre:
    st.success(f"¡Hola, { nombre }! Tienes { edad } años y seleccionaste { genero } como género.")
    st.write(f"Tu nivel de satisfacción con esta aplicación es: { nivel_satisfaccion }/100")
  else:
    st.error("Por favor, introduce tu nombre antes de enviar.")

st.write("---")
st.write("Gracias por probar esta aplicación básica. ¡Esperamos que te haya gustado!")
