import cv2
import numpy as np
import matplotlib.pyplot as plt

# cargar la imagen
image = cv2.imread("../Recursos/goku.jpg")

# aplicar filto Gausiano con un kernel de 5x5
gaussian_image = cv2.GaussianBlur(image, (5, 5), 0)

# mostrar los resultados
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Imagen original")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.subplot(1, 2, 2)
plt.title("Imagen suavizada (Gaussian Blur)")
plt.imshow(cv2.cvtColor(gaussian_image, cv2.COLOR_BGR2RGB))
plt.show()
