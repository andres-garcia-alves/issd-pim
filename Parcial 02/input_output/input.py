import cv2
from PIL import Image
from enum import Enum

# Directorio de entrada
base_path = "./data/input/"

# Enumeraciones para las 'imágenes', 'gifs' y 'videos'
# - sirven para tipificar el archivo a cargar, en lugar de usar un string cualquiera)
# - evita errores de tipeo y mejora la legibilidad del código
class Images(Enum):
  Dado = "dado.jpg"
  Goku = "goku.jpg"
  Pelota = "pelota.jpg"
  Pelota2 = "pelota2.jpg"

class Gifs(Enum):
  Homero = "homero.gif"

class Videos(Enum):
  Atomic_Bomb = "atomic_bomb.mp4"
  BabyYoda = "baby_yoda.mp4"
  BackToTheFuture = "back_to_the_future.mp4"
  Fury = "fury.mp4"
  Teletubies = "teletubies.mp4"


# Cargar y retornar una imagen
def load_image(image: Images = Images.Goku):
  return cv2.imread(base_path + image.value)


# Cargar y retornar un gif animado
def load_gif(gif: Gifs = Gifs.Homero):
  return Image.open(base_path + gif.value)


# Cargar y retornar un video
def load_video(video: Videos = Videos.Fury):
  return cv2.VideoCapture(base_path + video.value)
