import numpy as np
from PIL import Image, ImageSequence
import cv2

from input_output import input, output
from processing import processing

# -----------------------------------------------------------------
# Ejemplo de Super-Resolución para gif animados (con PIL + OpenCV)
# -----------------------------------------------------------------

path_output = "./data/output/03-imagen-gif-animado/"

file_name_output = "homero_alta_res.gif"

# Cargar el GIF original con PIL
gif = input.load_gif()

# Crear objeto de superresolución
sr = cv2.dnn_superres.DnnSuperResImpl_create()

# Cargar el modelo
sr.readModel(processing.path_models + "ESPCN_x2.pb")   # opción ligera, calidad media
# sr.readModel(processing.path_models + "EDSR_x2.pb")  # opción pesada, muy alta calidad	

# Establecer el modelo y la escala (2x, 3x, 4x, 8x)
sr.setModel("espcn", 2)
# sr.setModel("edsr", 2)

# Lista para guardar los nuevos frames procesados
frames_sr = []

# Procesar cada cuadro del GIF (PIL)
for frame in ImageSequence.Iterator(gif):
    
  # Convertir a array de OpenCV (RGB -> BGR)
  frame_cv = cv2.cvtColor(np.array(frame.convert("RGB")), cv2.COLOR_RGB2BGR)

  # Aplicar superresolución
  frame_sr = sr.upsample(frame_cv)

  # Convertir de nuevo a PIL (BGR -> RGB)
  frame_pil = Image.fromarray(cv2.cvtColor(frame_sr, cv2.COLOR_BGR2RGB))

  # Añadir el frame procesado a la lista
  frames_sr.append(frame_pil)

# Guardar el nuevo GIF re-escalado
frames_sr[0].save(
  path_output + file_name_output,
  save_all=True,
  append_images=frames_sr[1:],
  duration=gif.info.get('duration', 100),
  loop=0
)

print('Trabajo terminado.')
