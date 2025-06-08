from input_output import input, output
from processing import core_processing, image_processing

# ------------------------------------------------------------
# Ejemplo Básico de Super-Resolución de imágenes (con OpenCV)
#
# - familia FSRCNN-small: modelo ligero, calidad baja
# - familia FSRCNN:       modelo ligero, calidad media
# - familia ESPCN:        modelo ligero, calidad media
# - familia LapSRN:       modelo ligero, calidad alta
# - familia EDSR:         modelo pesado, calidad muy alta
# ------------------------------------------------------------

# Cargar la imagen original
img = input.load_image(input.Images.Goku)

# Instanciar y configurar un modelo de super-resolución
sr = core_processing.sr_create_model(core_processing.Models.LapSRN_x8)  # opción ligera, calidad alta
# sr = core_processing.sr_create_model(core_processing.Models.EDSR_x3)  # opción pesada, calidad muy alta

# Aplicar la super-resolución
img_scaled = image_processing.scale(sr, img)

# Guardar y mostrar el resultado
output.save_image(img_scaled, "goku_alta_res", output.Exercise.One)
output.show_image(img_scaled, "Resultado")
output.done()
