import cv2

# Cargar las imágenes
img_original = cv2.imread("./input/imagen-input.jpg")
img_glasses = cv2.imread("./input/anteojos-de-sol.png", cv2.IMREAD_UNCHANGED)

# Detectar rostros en la imagen
gray = cv2.cvtColor(img_original, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

# Para cada rostro detectado, dibujar un rectángulo y superponer los anteojos de sol
for (x, y, w, h) in faces:

  # Dibujar un rectángulo alrededor del rostro detectado
  cv2.rectangle(img_original, (x, y), (x+w, y+h), (0, 255, 0), 2)

  # Redimensionar los anteojos de sol al tamaño del rostro detectado
  img_glasses_resized = cv2.resize(img_glasses, (w, h))

  # Separar los canales de la imagen de los anteojos
  img_glasses_bgr = img_glasses_resized[:, :, :3]   # Los canales BGR
  img_glasses_alpha = img_glasses_resized[:, :, 3]  # El canal alfa (transparencia)

  # La posición de los anteojos
  x_offset = x
  y_offset = y - int(h * 0.05)

  # Verificar que los índices no se salgan del rango de la imagen de fondo
  # Extraer la región de la imagen de fondo donde se pondrán los anteojos
  y1, y2 = max(y_offset, 0), min(y_offset + h, img_original.shape[0])
  x1, x2 = max(x_offset, 0), min(x_offset + w, img_original.shape[1])
  roi = img_original[y1:y2, x1:x2]

  # Crear la máscara de los anteojos basada en la transparencia (canal alfa)
  alpha_glasses_resized = img_glasses_alpha[y1-y_offset:y2-y_offset, x1-x_offset:x2-x_offset]
  mask = alpha_glasses_resized / 255.0  # Normalizar la máscara entre 0 y 1

  # Mezclar los anteojos con el fondo usando la máscara
  for channel in range(0, 3):
    roi[:, :, channel] = roi[:, :, channel] * (1 - mask) + img_glasses_bgr[y1 - y_offset:y2 - y_offset, x1 - x_offset:x2 - x_offset, channel] * mask

  # Poner la región modificada de vuelta en la imagen original
  img_original[y1:y2, x1:x2] = roi

# Mostrar la imagen resultante
cv2.imwrite('./output/imagen-output.jpg', img_original)
cv2.imshow('Deteccion de rostros', img_original)
cv2.waitKey(0)
cv2.destroyAllWindows()
