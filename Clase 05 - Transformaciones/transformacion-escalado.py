import cv2
import numpy as np
import matplotlib.pyplot as plt

# cargar la imagen
image = cv2.imread("../recursos/goku.jpg")
rows, cols = image.shape[:2]

# redimensionar la imagen
scaled_image = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

# mostrar los resultados
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Imagen original")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.subplot(1, 2, 2)
plt.title("Imagen rotada")
plt.imshow(cv2.cvtColor(scaled_image, cv2.COLOR_BGR2RGB))
plt.show()
