import cv2
import numpy as np
import matplotlib.pyplot as plt

# cargar la imagen
image = cv2.imread("../recursos/goku.jpg", cv2.IMREAD_GRAYSCALE)

# aplicar filto Canny
canny_image = cv2.Canny(image, 100, 200)

# mostrar los resultados
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Imagen original (grises)")
plt.imshow(image, cmap="gray")
plt.subplot(1, 2, 2)
plt.title("Bordes detectados (Canny)")
plt.imshow(canny_image, cmap="gray")
plt.show()
