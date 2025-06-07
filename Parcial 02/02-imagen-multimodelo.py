import cv2

from input_output import input, output
from processing import processing

# -----------------------------------------------------------------
# Ejemplo Multimodelo de Super-Resolución de imágenes (con OpenCV)
# -----------------------------------------------------------------

path_output = "./data/output/02-imagen-multimodelo/"

# Diccionario con los modelos y sus escalas disponibles


# Cargar la imagen original
img = input.load_image()

# Crear la instancia para superresolución
sr = cv2.dnn_superres.DnnSuperResImpl_create()

for model in processing.models:
  for escala in processing.models[model]:

    # Cargar el modelo
    sr.readModel(processing.path_models + f"{ model }_x{ escala }.pb")
    
    # Establecer el modelo y la escala (2x, 3x, 4x, 8x)
    sr.setModel(model, escala)
    
    # Aplicar superresolución
    img_scaled = sr.upsample(img)
    
    # Guardar el resultado
    file_name = f"{ model }_x{ escala }_alta_res.jpg"
    output.save_image(img_scaled, file_name, output.Exercise.Two)
    
output.done()
