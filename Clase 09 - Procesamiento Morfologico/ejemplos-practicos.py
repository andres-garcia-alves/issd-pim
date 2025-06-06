import numpy as np
import matplotlib.pyplot as plt
import cv2

imagen = cv2.imread("../Recursos/goku.jpg", cv2.IMREAD_GRAYSCALE)

# aplicar un umbral para asegurar que sea binaria
_, imagen_bin = cv2.threshold(imagen, 127, 255, cv2.THRESH_BINARY)

# definir elemento estructurante
kernel = np.ones((5,5), np.uint8)

# aplicar erosión para separar objetos conectados
erosion = cv2.erode(imagen_bin, kernel, iterations=1)

# aplicar dilatación para recuperar estructuras
dilatacion = cv2.dilate(erosion, kernel, iterations=1)

# mostrar resultados
fig, axs = plt.subplots(1, 3, figsize=(15,5))
axs[0].imshow(imagen_bin, cmap="gray")
axs[0].set_title("Imagen Binaria")
axs[0].axis("off")

axs[1].imshow(erosion, cmap="gray")
axs[1].set_title("Después de la Erosión")
axs[1].axis("off")

axs[2].imshow(dilatacion, cmap="gray")
axs[2].set_title("Después de la Dilatación")
axs[2].axis("off")

plt.show()
