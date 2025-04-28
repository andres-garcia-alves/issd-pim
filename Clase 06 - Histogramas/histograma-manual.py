import numpy as np
import matplotlib.pyplot as plt
import cv2

# calculo manual del histograma
def calcular_histograma_manual(imagen):
  histograma = np.zeros(256, dtype=int)

  for fila in imagen:
    for intensidad in fila:
      histograma[intensidad] += 1
  
  return histograma


# cargar la imagen
imagen = cv2.imread("../Recursos/goku.jpg", cv2.IMREAD_GRAYSCALE)

# calcular el histograma
histograma = calcular_histograma_manual(imagen)
print(histograma)

# mostrar la imagen original
cv2.imshow("Imagen Original", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

# mostrar su histograma
plt.figure(figsize=(10, 5))
plt.bar(range(256), histograma, color="gray")
plt.title("Histograma Manual")
plt.xlabel("Niveles de intensidad")
plt.ylabel("Frecuencia")
plt.grid()
plt.show()
