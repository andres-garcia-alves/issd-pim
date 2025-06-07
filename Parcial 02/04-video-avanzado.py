from input_output import input, output
from processing import core_processing, video_processing

# -----------------------------------------------------
# Ejemplo de Super-Resolución para videos (con OpenCV)
# -----------------------------------------------------

# Cargar el video
video = input.load_video(input.Videos.Fury)

# Instanciar y configurar un modelo de super-resolución
sr = core_processing.sr_create_model(core_processing.Models.LapSRN_x4)  # opción ligera, calidad alta
# sr = core_processing.sr_create_model(core_processing.Models.EDSR_x4)  # opción pesada, calidad muy alta

# Obtener las propiedades del video y calcular el tamaño de salida
fps, input_width, input_height = video_processing.get_video_properties(video)
output_width, output_height = video_processing.calculate_output_size(input_width, input_height, scale=4)

# Crear el encoder de video (MPEG-4)
mp4_encoder = video_processing.build_mp4_encoder()

# Crear el buffer de salida
file_name = output.get_video_full_name(input.Videos.Fury)
output_buffer = video_processing.create_output_buffer(file_name, mp4_encoder, fps, output_width, output_height)

# Procesar los frames
i = 0
while video.isOpened():

  # Leer de a 1 frame a la vez, y detener el bucle ('break') cuando ya no queden más
  ret, frame = video.read()
  if not ret: break

  # Aplicar la super-resolución
  frame_sr = sr.upsample(frame)

  # opcional: guardar los frames individuales
  output.save_video_frame(frame_sr, f"frame_{i:04d}")
  i += 1

  # Escribir el nuevo frame al buffer de salida
  output_buffer.write(frame_sr)

# Liberar los recursos de la memoria
video_processing.release_resources([video, output_buffer])
