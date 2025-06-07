import cv2

from input_output import input, output
from processing import processing

# ------------------------------------------------------------
# Ejemplo Básico de Super-Resolución de imágenes (con OpenCV)
#
# - familia ESPCN:        modelo ligero, calidad media
# - familia FSRCNN:       modelo ligero, calidad media
# - familia FSRCNN-small: modelo ligero, calidad baja
# - familia LapSRN:       modelo ligero, alta calidad
# - familia EDSR:         modelo pesado, muy alta calidad
# ------------------------------------------------------------

# Cargar la imagen original
img = input.load_image()

# Crear la instancia para superresolución
sr = cv2.dnn_superres.DnnSuperResImpl_create()

# Cargar el modelo
sr.readModel(processing.path_models + "LapSRN_x8.pb")  # opción ligera, alta calidad
# sr.readModel(processing.path_models + "EDSR_x3.pb")  # opción pesada, muy alta calidad

# Establecer el modelo y la escala (2x, 3x, 4x, 8x)
sr.setModel("lapsrn", 8)
# sr.setModel("edsr", 3)

# Aplicar superresolución
img_scaled = sr.upsample(img)

# Guardar y mostrar resultado
output.save_image(img_scaled, "goku_alta_res", output.Exercise.One)
output.show_image(img_scaled, "Resultado")
output.done()
