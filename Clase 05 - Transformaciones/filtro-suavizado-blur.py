import cv2
import numpy as np
import matplotlib.pyplot as plt

# cargar la imagen
image = cv2.imread("../recursos/goku.jpg")

# aplicar filto Blur (promedio) con un kernel de 5x5
blur_image = cv2.blur(image, (5, 5))

# mostrar los resultados
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Imagen original")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.subplot(1, 2, 2)
plt.title("Imagen suavizada (Blur)")
plt.imshow(cv2.cvtColor(blur_image, cv2.COLOR_BGR2RGB))
plt.show()
