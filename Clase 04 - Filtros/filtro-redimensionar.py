import cv2

imagen = cv2.imread("../recursos/goku.jpg")

ancho, alto = (1092, 736)    # escalado x4, original 273x184
imagen_redim1 = cv2.resize(imagen, (ancho, alto), interpolation=cv2.INTER_NEAREST)
imagen_redim2 = cv2.resize(imagen, (ancho, alto), interpolation=cv2.INTER_LINEAR)
imagen_redim3 = cv2.resize(imagen, (ancho, alto), interpolation=cv2.INTER_CUBIC)
imagen_redim4 = cv2.resize(imagen, (ancho, alto), interpolation=cv2.INTER_LANCZOS4)

cv2.imshow("Imagen redimensionada (INTER_NEAREST)", imagen_redim1)
cv2.imshow("Imagen redimensionada (INTER_LINEAR)", imagen_redim2)
cv2.imshow("Imagen redimensionada (INTER_CUBIC)", imagen_redim3)
cv2.imshow("Imagen redimensionada (INTER_LANCZOS4)", imagen_redim4)

cv2.waitKey(0)
cv2.destroyAllWindows()
