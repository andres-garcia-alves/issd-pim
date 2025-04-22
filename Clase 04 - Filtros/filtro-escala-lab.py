import cv2

imagen = cv2.imread("../recursos/goku.jpg")

imagen_lab = cv2.cvtColor(imagen, cv2.COLOR_BGR2LAB)
l, a, b = cv2.split(imagen_lab)

cv2.imshow("Canal Luminosidad (L)", l)  # luminosidad
cv2.imshow("Canal Color A (A)", a)      # color a
cv2.imshow("Canal Color B (B)", b)      # color b

cv2.waitKey(0)
cv2.destroyAllWindows()
