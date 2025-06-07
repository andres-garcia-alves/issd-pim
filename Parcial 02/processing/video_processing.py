import cv2

# Obtener las propiedades del video
def get_video_properties(video):
  fps = video.get(cv2.CAP_PROP_FPS)
  frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
  frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

  return fps, frame_width, frame_height


# Calcular el tamaño de salida según la escala
def calculate_output_size(frame_width, frame_height, scale=2):
  return frame_width * scale, frame_height * scale


# Crear el encoder de video (MPEG-4)
def build_mp4_encoder():
  return cv2.VideoWriter_fourcc(*'mp4v')  # *'mp4v' -> 'm','p','4','v' 


# Crear un buffer de salida
def create_output_buffer(file_name, mp4_encoder, fps, output_width, output_height):
  return cv2.VideoWriter(file_name, mp4_encoder, fps, (output_width, output_height))


# Liberar los recursos de la memoria
def release_resources(resources):
  for resource in resources:
    resource.release()
