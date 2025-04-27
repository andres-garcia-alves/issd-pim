import cv2

imagen = cv2.imread("../Recursos/goku.jpg")

imagen_grises = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

cv2.imshow("Imagen original", imagen)
cv2.imshow("Imagen en escala de grises", imagen_grises)

cv2.waitKey(0)
cv2.destroyAllWindows()
