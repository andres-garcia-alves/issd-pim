import cv2
from enum import Enum
from input_output import input

# Directorios de salida
output_path_01 = "./data/output/01-imagen-basico/"
output_path_02 = "./data/output/02-imagen-multimodelo/"
output_path_03 = "./data/output/03-imagen-gif-animado/"
output_path_04 = "./data/output/04-video-avanzado/"

# Enumeraciones para los 'ejercicios'
# - sirven para tipificar el ejercicio en cuestión, en lugar de usar un string cualquiera)
# - evita errores de tipeo y mejora la legibilidad del código
class Exercise(Enum):
  One = 1
  Two = 2
  Three = 3
  Four = 4


# Mostrar una imagen por pantalla
def show_image(image, title="imagen"):
  cv2.imshow(title, image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()


# Mostrar varias imagenes por pantalla
def show_images(images, title="imagenes"):
  for image in images:
    cv2.imshow(title, image)
    cv2.waitKey(0)
  cv2.destroyAllWindows()


# Guardar una imagen
def save_image(img, name, exercise):
  full_name = ""
  if exercise == Exercise.One:    full_name = output_path_01 + name + ".jpg"
  elif exercise == Exercise.Two:  full_name = output_path_02 + name + ".jpg"
  else:                           Exception("exercise inválido.")

  cv2.imwrite(full_name, img)


# Guardar un gif animado
def save_gif(frames, name, duration):
  full_name = output_path_03 + name + ".gif"
  frames[0].save(full_name, save_all=True, append_images=frames[1:], duration=duration, loop=1)


# Construir el path y nombre completo de un video
def get_video_full_name(input_video: input.Videos = input.Videos.Fury):
  video_name = input_video.value.split(".")[0]
  video_ext = input_video.value.split(".")[1]

  return output_path_04 + video_name + "_alta_res" + "." + video_ext


# Guardar un frame de un video
def save_video_frame(img, name):
  full_name = output_path_04 + "frames/" + name + ".jpg"
  cv2.imwrite(full_name, img)


# Mensaje de finalización
def done(msg="Trabajo terminado."):
  print(msg)
