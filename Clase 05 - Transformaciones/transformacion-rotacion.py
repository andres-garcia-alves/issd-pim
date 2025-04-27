import cv2
import numpy as np
import matplotlib.pyplot as plt

# cargar la imagen
image = cv2.imread("../Recursos/goku.jpg")
rows, cols = image.shape[:2]

# definir el punto de rotacion (centro de la imagen) y el angulo
center = (cols // 2, rows // 2)
angle = 45  # rotar 45 grados
scale = 1   # tamaño original

# crear la matriz de rotacion
M = cv2.getRotationMatrix2D(center, angle, scale)

# aplicar la transformacion usando la matriz
rotated_image = cv2.warpAffine(image, M, (cols, rows))

# mostrar los resultados
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Imagen original")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.subplot(1, 2, 2)
plt.title("Imagen rotada")
plt.imshow(cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB))
plt.show()
