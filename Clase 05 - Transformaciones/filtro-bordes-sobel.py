import cv2
import numpy as np
import matplotlib.pyplot as plt

# cargar la imagen
image = cv2.imread("../recursos/goku.jpg", cv2.IMREAD_GRAYSCALE)

# aplicar filto Sobel en dirección horizontal y vertical
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# calcular la magnitud combinada de los bordes
sobel_combined = cv2.magnitude(sobel_x, sobel_y)

# mostrar los resultados
plt.figure(figsize=(16, 6))
plt.subplot(1, 4, 1)
plt.title("Imagen original (grises)")
plt.imshow(image, cmap="gray")
plt.subplot(1, 4, 2)
plt.title("Sobel X")
plt.imshow(sobel_x, cmap="gray")
plt.subplot(1, 4, 3)
plt.title("Sobel Y")
plt.imshow(sobel_y, cmap="gray")
plt.subplot(1, 4, 4)
plt.title("Sobel combinado")
plt.imshow(sobel_combined, cmap="gray")
plt.show()
