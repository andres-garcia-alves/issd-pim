from enum import Enum
import cv2

output_path_01 = "./data/output/01-imagen-basico/"
output_path_02 = "./data/output/02-imagen-multimodelo/"
output_path_03 = "./data/output/03-imagen-gif-animado/"
output_path_04 = "./data/output/04-video-avanzado/"

class Exercise(Enum):
  One = 1
  Two = 2
  Three = 3
  Four = 4


def show_image(img, title="imagen"):
  cv2.imshow(title, img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()


def save_image(img, name, exercise):
  file_path = ""
  if exercise == Exercise.One:    file_path = output_path_01 + name + ".jpg"
  elif exercise == Exercise.Two:  file_path = output_path_02 + name + ".jpg"
  else:                           Exception("exercise inválido.")

  cv2.imwrite(file_path, img)


def save_gif(gif, name):
  Exception("Falta implementar.")


def save_video(video, name):
  Exception("Falta implementar.")


def done(msg="Trabajo Terminado"):
  print(msg)
