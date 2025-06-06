import cv2

def main():

  image = cv2.imread("../Recursos/personas.jpg")

  if image is None:
    print("No se pudo cargar la imagen. Revisa la ruta o el nombre del archivo.")
    return

  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # detectar rostros en la imagen
  # - scaleFactor: factor de reducción de la imagen en cada escala (1.3 suele dar buenos resultados)
  # - minNeighbors: número de vecinos para ser considerado un rostro válido
  face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
  faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

  # dibujar rectángulos alrededor de los rostros detectados
  for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

  # mostrar la imagen resultante
  cv2.imshow('Rostros detectados', image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

if __name__ == '__main__':
  main()
