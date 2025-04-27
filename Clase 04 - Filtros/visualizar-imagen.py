# EJEMPLO CON CV2
import cv2

imagen1 = cv2.imread("../Recursos/goku.jpg")
print("CV2 Dimesiones (ancho, alto, canales):", imagen1.shape)

# mostar la imagen en una ventana
cv2.imshow("CV2 - Mostrar imagen", imagen1)
cv2.waitKey(0)
cv2.destroyAllWindows()


# EJEMPLO CON PILLOW
from PIL import Image

imagen2 = Image.open("../Recursos/goku.jpg")
print("Pillow Tamaño:", imagen1.size)

imagen2.show()


# EJEMPLO CON MATPLOTLIB
import matplotlib.pyplot as plt

imagen3 = cv2.imread("../Recursos/goku.jpg", )
imagen3_rgb = cv2.cvtColor(imagen3, cv2.COLOR_BGR2RGB)

# plt.imshow(imagen3)
plt.imshow(imagen3_rgb)
plt.title("MATPLOTLIB - Mostrar imagen")
plt.axis("off")
plt.show()
