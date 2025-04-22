import cv2

imagen = cv2.imread("../recursos/goku.jpg")

imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(imagen_hsv)

cv2.imshow("Canal Hue (H)", h)        # tono/matiz como ángulo (0° =rojo, 120° = verde, 240° = azul)
cv2.imshow("Canal Saturation (S)", s) # cantidad de color (0% = gris, 100% = color puro)
cv2.imshow("Canal Value (V)", v)      # brillo (0% = negro, 100% = blanco)

cv2.waitKey(0)
cv2.destroyAllWindows()
