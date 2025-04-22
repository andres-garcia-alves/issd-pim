import cv2

imagen = cv2.imread("../recursos/goku.jpg")

x1, y1 = (50, 25)               # punto superior-izquierdo
x2, y2 = (x1 + 175, y1 + 100)   # punto inferior-derecho

imagen_recortada = imagen[y1:y2, x1:x2] # formato: [filas, columnas]

cv2.imshow("Imagen recortada", imagen_recortada)

cv2.waitKey(0)
cv2.destroyAllWindows()
