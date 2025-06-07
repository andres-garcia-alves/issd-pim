from enum import Enum
import cv2

base_path = "./data/input/"

image_file_name = "goku.jpg"
gif_file_name = "homero.gif"
video_file_name = "furia.mp4"

class Images(Enum):
  Goku = "goku.jpg"

class Gifs(Enum):
  Homero = "homero.gif"

class Videos(Enum):
  Atomic_Bomb = "atomic_bomb.mp4"
  BabyYoda = "baby_yoda.mp4"
  BackToTheFuture = "back_to_the_future.mp4"
  Fury = "fury.mp4"
  Teletubies = "teletubies.mp4"


def load_image(image: Images = Images.Goku):
  return cv2.imread(base_path + image_file_name)


def load_gif(gif: Gifs = Gifs.Homero):
  return cv2.imread(base_path + gif_file_name)


def load_video(video: Videos = Videos.Fury):
  return cv2.imread(base_path + video_file_name)
