import numpy as np
from PIL import Image, ImageSequence
import cv2

from input_output import input, output
from processing import core_processing

# -----------------------------------------------------------------
# Ejemplo de Super-Resolución para gif animados (con PIL + OpenCV)
# -----------------------------------------------------------------

# Cargar el GIF original con PIL
gif = input.load_gif(input.Gifs.Homero)

# Instanciar y configurar un modelo de super-resolución
sr = core_processing.sr_create_model(core_processing.Models.ESPCN_x2)   # opción ligera, calidad media
# sr = core_processing.sr_create_model(core_processing.Models.EDSR_x2)  # opción pesada, calidad muy alta

# Lista para guardar los nuevos frames procesados
frames_sr = []

# Iterar sobre cada cuadro del gif animado (PIL)
for frame in ImageSequence.Iterator(gif):
    
  # Convertir a array de OpenCV (RGB -> BGR)
  frame_cv = cv2.cvtColor(np.array(frame.convert("RGB")), cv2.COLOR_RGB2BGR)

  # Aplicar la super-resolución
  frame_sr = sr.upsample(frame_cv)

  # Convertir de nuevo a PIL (BGR -> RGB)
  frame_pil = Image.fromarray(cv2.cvtColor(frame_sr, cv2.COLOR_BGR2RGB))

  # Añadir el frame procesado a la lista
  frames_sr.append(frame_pil)

# Guardar el nuevo GIF re-escalado
duration = gif.info.get('duration', 100)
output.save_gif(frames_sr, "homero_alta_res", duration)

output.done()
