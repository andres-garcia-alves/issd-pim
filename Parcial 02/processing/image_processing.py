import numpy as np
from PIL import Image
import cv2


def get_coordinate(img):
  coordinate = []                                     # para guardar la coordenada seleccionada
  window_title = "Seleccionar una Zona de la Imagen"  # título de la ventana

  # Esta función se activa cuando se hace clic con el mouse sobre la imagen
  def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:                # detectar un clic izquierdo
      print(f"Coordenada: x={ x }, y={ y }")          # imprime la coordenada seleccionada
      coordinate.append((x, y))                       # guardar la coordenada
      cv2.destroyAllWindows()                         # cerrar la ventana tras la selección
  
  cv2.imshow(window_title, img)                       # mostrar la imagen y esperar interacción
  cv2.setMouseCallback(window_title, click_event)     # asocia función al clic del mouse
  cv2.waitKey(0)                                      # espera hasta que se presione una tecla

  return coordinate[0]                                # devuelve la coordenada (x, y)


# Esta función realiza el proceso de inpainting sobre una imagen.
# A partir de una coordenada y un radio, genera una máscara y aplica CV2 para reconstruir visualmente esa zona.
def apply_inpainting(image, center, radius=40):

  # Crear una máscara en negro con el mismo tamaño que la imagen (1 canal)
  mask = np.zeros(image.shape[:2], dtype=np.uint8)

  # Dibujar un círculo blanco en la máscara que indica la zona a rellenar
  cv2.circle(mask, center, radius, 255, -1)

  # Aplicar el algoritmo de inpainting con el método TELEA
  resultado = cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)

  # Devolver la imagen resultante y la máscara usada
  return resultado, mask


def scale(sr, image):
  return sr.upsample(image)


def pil_to_cv2(image):
  return cv2.cvtColor(np.array(image.convert("RGB")), cv2.COLOR_RGB2BGR)


def cv2_to_pil(image):
  return Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
