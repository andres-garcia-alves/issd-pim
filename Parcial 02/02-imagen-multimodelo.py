from input_output import input, output
from processing import core_processing

# -----------------------------------------------------------------
# Ejemplo Multimodelo de Super-Resolución de imágenes (con OpenCV)
# -----------------------------------------------------------------

# Cargar la imagen original
img = input.load_image(input.Images.Goku)

# Diccionario con los modelos y sus escalas disponibles
for model in core_processing.Models:

    # Instanciar y configurar un modelo de super-resolución
    sr = core_processing.sr_create_model(model)

    # Aplicar la super-resolución
    img_scaled = sr.upsample(img)
    
    # Guardar el resultado
    file_name = model.value.lower() + "_alta_res"
    output.save_image(img_scaled, file_name, output.Exercise.Two)
    
output.done()
