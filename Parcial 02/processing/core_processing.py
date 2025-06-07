import cv2
from enum import Enum

# Directorio con los modelos de super-resolución
path_models = "./models/"

# Diccionario con los modelos y sus escalas disponibles
models = {
  "fsrcnn": [2, 3, 4],
  "espcn":  [2, 3, 4],
  "lapsrn": [2, 4, 8],
  "edsr":   [2, 3, 4]
}

# Enumeraciones para los 'modelos pre-entrenados'
# - sirven para tipificar el archivo a cargar, en lugar de usar un string cualquiera)
# - ayuda a evitar errores de tipeo y mejora la legibilidad del código
class Models(Enum):
  FSRCNN_x2 = "FSRCNN_x2"
  FSRCNN_x3 = "FSRCNN_x3"
  FSRCNN_x4 = "FSRCNN_x4"
  ESPCN_x2 = "ESPCN_x2"
  ESPCN_x3 = "ESPCN_x3"
  ESPCN_x4 = "ESPCN_x4"
  LapSRN_x2 = "LapSRN_x2"
  LapSRN_x4 = "LapSRN_x4"
  LapSRN_x8 = "LapSRN_x8"
  EDSR_x2 = "EDSR_x2"
  EDSR_x3 = "EDSR_x3"
  EDSR_x4 = "EDSR_x4"


# Instanciar y configurar un modelo de super-resolución
def sr_create_model(model: Models = Models.LapSRN_x2):
  model_name = model.value.split("_")[0].lower()    # extraer el nombre del modelo (ej: 'LapSRN')
  model_scale = int(model.value.split("_")[1][1])   # extraer la escala (ej: 2, 3, 4, 8)

  # Crear la instancia CV2 de super-resolución
  sr = cv2.dnn_superres.DnnSuperResImpl_create()

  # Cargar un modelo
  sr.readModel(path_models + model.value + '.pb')

  # Configurar en CV2 el modelo cargado y su escala (2x, 3x, 4x, 8x)
  sr.setModel(model_name, model_scale)

  print(f"Modelo cargado: { model.name }")
  return sr
