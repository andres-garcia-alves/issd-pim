import numpy as np
import cv2

# Función para agregar anteojos de sol a los rostros detectados en un frame
def add_glases_to_faces(frame, glasses, faces):

  # Verificar si se detectaron rostros, sino retornar el frame original
  if len(faces) == 0: return frame

  # Buscar el rostro detectado de mayor tamaño
  biggest = 0
  biggest_idx = 0
  sizes = [w * h for (x, y, w, h) in faces]

  for i in range(len(sizes)):
    if sizes[i] > biggest:
      biggest = sizes[i]
      biggest_idx = i

  # Extraer sus coordenadas
  (x, y, w, h) = faces[biggest_idx]

  # Dibujar un rectángulo alrededor del rostro detectado
  cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)

  # Omitir los anteojos de sol si el rostro es demasiado pequeño
  print(f"Tamaño del rostro detectado: { w }x{ h } = { w * h }")
  if w * h < 20000: return frame

  # Recudir el tamaño de los anteojos de sol al 90%
  w = int(w * 0.9)
  h = int(h * 0.9)

  # Redimensionar los anteojos de sol al tamaño del rostro detectado
  glasses_resized = cv2.resize(glasses, (w, h))

  # Separar los canales de la imagen de los anteojos
  glasses_bgr = glasses_resized[:, :, :3]   # Los canales BGR
  glasses_alpha = glasses_resized[:, :, 3]  # El canal alfa (transparencia)

  # La posición de los anteojos
  x_offset = x
  y_offset = y

  # Verificar que los índices no se salgan del rango de la imagen de fondo
  # Extraer la región de la imagen de fondo donde se pondrán los anteojos
  y1, y2 = max(y_offset, 0), min(y_offset + h, frame.shape[0])
  x1, x2 = max(x_offset, 0), min(x_offset + w, frame.shape[1])
  roi = frame[y1:y2, x1:x2]

  # Crear la máscara de los anteojos basada en la transparencia (canal alfa)
  alpha_glasses_resized = glasses_alpha[y1-y_offset:y2-y_offset, x1-x_offset:x2-x_offset]
  mask = alpha_glasses_resized / 255.0  # Normalizar la máscara entre 0 y 1

  # Mezclar los anteojos con el fondo usando la máscara
  for channel in range(0, 3):
    roi[:, :, channel] = roi[:, :, channel] * (1 - mask) + glasses_bgr[y1 - y_offset:y2 - y_offset, x1 - x_offset:x2 - x_offset, channel] * mask

  # Poner la región modificada de vuelta en la imagen original
  frame[y1:y2, x1:x2] = roi

  return frame


def main():

  # Cargar el video y la imagen
  video = cv2.VideoCapture("./input/video-input.mp4")
  glasses = cv2.imread("./input/anteojos-de-sol.png", cv2.IMREAD_UNCHANGED)

  # Crear el encoder de video (MPEG-4)
  mp4_encoder = cv2.VideoWriter_fourcc(*'mp4v')
  fps = video.get(cv2.CAP_PROP_FPS)
  frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
  frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

  # Crear el buffer de salida
  output_buffer = cv2.VideoWriter("./output/video-output.mp4", mp4_encoder, fps, (frame_width, frame_height))

  # Cargar el clasificador de rostros
  face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

  # Procesar los frames
  i = 0
  while video.isOpened():

    # Leer de a 1 frame a la vez, y detener el bucle cuando ya no queden más
    ret, frame = video.read()
    if not ret: break

    # Detectar rostros en la imagen
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(frame_gray, scaleFactor=1.1, minNeighbors=0) # scaleFactor=1.3, minNeighbors=5

    # Agregar los anteojos de sol a los rostros detectados  
    frame_modified = add_glases_to_faces(frame, glasses, faces)

    # guardar los frames individuales
    # frame_full_name = "./output/frames/" + f"frame_{i:04d}" + ".jpg"
    # cv2.imwrite(frame_full_name, frame_modified)
    # i += 1

    # Escribir el nuevo frame al buffer de salida
    output_buffer.write(frame_modified)

  video.release()
  output_buffer.release()


# ejecutar el programa principal
main()