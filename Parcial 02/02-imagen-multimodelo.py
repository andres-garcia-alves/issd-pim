import cv2

# -----------------------------------------------------------------
# Ejemplo Multimodelo de Super-Resolución de imágenes (con OpenCV)
# -----------------------------------------------------------------

path_models = "./models/"
path_input = "./input/"
path_output = "./output/02-imagen-multimodelo/"

# Diccionario con los modelos y sus escalas disponibles
models = {
  "espcn": [2, 3, 4],
  "fsrcnn": [2, 3, 4],
  "lapsrn": [2, 4, 8],
  "edsr": [2, 3, 4]
}

# Cargar la imagen original
img = cv2.imread(path_input + "goku.jpg")

# Crear la instancia para superresolución
sr = cv2.dnn_superres.DnnSuperResImpl_create()

for model in models:
  for escala in models[model]:

    # Cargar el modelo
    sr.readModel(path_models + f"{ model }_x{ escala }.pb")
    
    # Establecer el modelo y la escala (2x, 3x, 4x, 8x)
    sr.setModel(model, escala)
    
    # Aplicar superresolución
    img_scaled = sr.upsample(img)
    
    # Guardar el resultado
    output_path = f"{ path_output }{ model }_x{ escala }_alta_res.jpg"
    cv2.imwrite(output_path, img_scaled)
    
print('Trabajo terminado.')
