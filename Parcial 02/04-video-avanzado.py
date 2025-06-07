import cv2

from input_output import input, output
from processing import processing

# -----------------------------------------------------
# Ejemplo de Super-Resolución para videos (con OpenCV)
# -----------------------------------------------------

path_output = "./data/output/04-video-avanzado/"

file_name_output = "furia_alta_res.mp4"

# Cargar el video
video = input.load_video()

# Crear la instancia para superresolución
sr = cv2.dnn_superres.DnnSuperResImpl_create()

# Cargar el modelo
sr.readModel(processing.path_models + "LapSRN_x4.pb")  # opción ligera, alta calidad
# sr.readModel(processing.path_models + "EDSR_x4.pb")  # opción pesada, muy alta calidad	

# Establecer el modelo y la escala (2x, 3x, 4x, 8x)
scale = 4
sr.setModel("lapsrn", scale)
# sr.setModel("edsr", scale)

# Obtener las propiedades del video
fps = video.get(cv2.CAP_PROP_FPS)
frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Tamaño de salida según la escala
out_width, out_height = frame_width * scale, frame_height * scale

# Crear el encoder de video y el buffer de salida
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # equivale a: 'm','p','4','v' (MPEG-4 video)
out = cv2.VideoWriter(path_output + file_name_output, fourcc, fps, (out_width, out_height))

# Procesar los frames
i = 0
while video.isOpened():

  # Leer un frame del video
  # y detener el bucle si ya no quedan más frames (break)
  ret, frame = video.read()
  if not ret: break

  # Aplicar superresolución
  frame_sr = sr.upsample(frame)

  # opcional: guardar los frames individuales
  cv2.imwrite(path_output + f"frames/frame_{i:04d}.jpg", frame_sr)
  i += 1

  # Escribir el nuevo frame al buffer de salida
  out.write(frame_sr)

# Liberar los recursos de la memoria
video.release()
out.release()
