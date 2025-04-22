import cv2

imagen = cv2.imread("../recursos/goku.jpg")

(h, w) = imagen.shape[:2]   # alto, ancho
centro = (w // 2, h // 2)   # centro de la imagen
angulo = 45                 # angulo de rotacion
scale = 0.5                 # achicar/agrandar

matriz_rotacion = cv2.getRotationMatrix2D(centro, angulo, scale)
imagen_rotada = cv2.warpAffine(imagen, matriz_rotacion, (h, w))

cv2.imshow("Imagen rotada", imagen_rotada)

cv2.waitKey(0)
cv2.destroyAllWindows()
