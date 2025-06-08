from PIL import ImageSequence

from input_output import input, output
from processing import core_processing, image_processing

# -----------------------------------------------------------------
# Ejemplo de Super-Resolución para gif animados (con PIL + OpenCV)
# -----------------------------------------------------------------

# Cargar el GIF original con PIL
gif = input.load_gif(input.Gifs.Homero)

# Instanciar y configurar un modelo de super-resolución
sr = core_processing.sr_create_model(core_processing.Models.ESPCN_x2)   # opción ligera, calidad media
# sr = core_processing.sr_create_model(core_processing.Models.EDSR_x2)  # opción pesada, calidad muy alta

# Lista para guardar los nuevos frames procesados
frames_output = []

# Iterar sobre cada cuadro del GIF animado (PIL)
for frame in ImageSequence.Iterator(gif):
    
  # Convertir a array de OpenCV (RGB -> BGR)
  frame_cv = image_processing.convert_pil_to_cv2(frame)

  # Aplicar la super-resolución
  frame_scaled = image_processing.scale(sr, frame_cv)

  # Convertir de nuevo a PIL (BGR -> RGB)
  frame_pil = image_processing.convert_cv2_to_pil(frame_scaled)

  # Añadir el frame procesado a la lista
  frames_output.append(frame_pil)

# Guardar el nuevo GIF re-escalado
duration = gif.info.get('duration', 100)
output.save_gif(frames_output, "homero_alta_res", duration)
output.done()
