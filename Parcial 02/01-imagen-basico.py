import cv2

# ------------------------------------------------------------
# Ejemplo Básico de Super-Resolución de imágenes (con OpenCV)
#
# - familia ESPCN:  modelo ligero, calidad media
# - familia FSRCNN: modelo ligero, calidad media
# - familia LapSRN: modelo ligero, alta calidad
# - familia EDSR:   modelo pesado, muy alta calidad
# ------------------------------------------------------------


path_models = "./models/"
path_input = "./input/"
path_output = "./output/01-imagen-basico/"

file_name_input = "goku.jpg"
file_name_output = "goku_alta_res.jpg"

# Cargar la imagen original
img = cv2.imread(path_input + file_name_input)

# Crear la instancia para superresolución
sr = cv2.dnn_superres.DnnSuperResImpl_create()

# Cargar el modelo
sr.readModel(path_models + "LapSRN_x8.pb")  # opción ligera, alta calidad
# sr.readModel(path_models + "EDSR_x3.pb")  # opción pesada, muy alta calidad

# Establecer el modelo y la escala (2x, 3x, 4x, 8x)
sr.setModel("lapsrn", 8)
# sr.setModel("edsr", 3)

# Aplicar superresolución
img_scaled = sr.upsample(img)

# Guardar y mostrar resultado
cv2.imwrite(path_output + file_name_output, img_scaled)
cv2.imshow("Resultado", img_scaled)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('Trabajo terminado.')
