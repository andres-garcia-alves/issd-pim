import numpy as np
from PIL import Image
import cv2


def scale(sr, image):
  return sr.upsample(image)

def pil_to_cv2(img):
  return cv2.cvtColor(np.array(img.convert("RGB")), cv2.COLOR_RGB2BGR)

def cv2_to_pil(img):
  return Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
