import matplotlib.pyplot as plt
import cv2

# cargar la imagen
imagen = cv2.imread("../Recursos/goku.jpg", cv2.IMREAD_GRAYSCALE)

# calcular el histograma
histograma = cv2.calcHist([imagen], [0], None, [256], [0, 256])
print("Histograma (como sale de CV2):", "\n", histograma[:5], "...", "\n")

# convertir histograma a una lista 1D
histograma = histograma.flatten()
print("Histograma aplanado:", "\n", histograma)

# mostrar la imagen original
cv2.imshow("Imagen Original", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

# mostrar su histograma
plt.figure(figsize=(10, 5))
plt.bar(range(256), histograma)
plt.title("Histograma con CV2")
plt.xlabel("Niveles de intensidad")
plt.ylabel("Frecuencia")
plt.grid()
plt.show()
