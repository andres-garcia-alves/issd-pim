from input_output import input, output
from processing import image_processing

# ------------------------------------------------------------
# Este script actúa como punto de entrada del programa.
# Coordina el flujo completo: carga una imagen, permite al usuario seleccionar un punto,
# aplica inpainting sobre esa zona y muestra los resultados.
# ------------------------------------------------------------

# Cargar la imagen original
img = input.load_image(input.Images.Pelota)
# img = input.load_image(input.Images.Dado)
# img = input.load_image(input.Images.Pelota2)

# Obtener la coordenada seleccionada por el usuario (clic en imagen)
center_coord = image_processing.get_coordinate(img.copy())  # Devuelve una tupla (x, y)

# Aplicar el algoritmo de inpainting usando la coordenada obtenida
# Devuelve imagen resultado y la máscara generada
img_result, mask = image_processing.apply_inpainting(img, center_coord)

# Guardar la imagen resultante
output.save_image(img_result, "relleno_huecos", output.Exercise.One)

# Mostrar las 3 imágenes: original, máscara y el resultado final
output.show_images([img, mask, img_result], ["Imagen Original", "Mascara", "Imagen con Relleno de Huecos"])
output.done()
