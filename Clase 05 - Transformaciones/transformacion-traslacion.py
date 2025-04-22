import cv2
import numpy as np
import matplotlib.pyplot as plt

# cargar la imagen
image = cv2.imread("../recursos/goku.jpg")
rows, cols = image.shape[:2]

# matriz de traslacion
M = np.float32([
    [1, 0, 100],
    [0, 1, 50]
])

# aplicar la transformacion usando la matriz
traslated_image = cv2.warpAffine(image, M, (cols, rows))

# mostrar los resultados
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Imagen original")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.subplot(1, 2, 2)
plt.title("Imagen trasladada")
plt.imshow(cv2.cvtColor(traslated_image, cv2.COLOR_BGR2RGB))
plt.show()
