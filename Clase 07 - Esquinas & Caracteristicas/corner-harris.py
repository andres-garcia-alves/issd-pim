import numpy as np
import cv2

# cargar la imagen y convertir a escala de grises
image_original = cv2.imread('../Recursos/goku.jpg')
image_gray = cv2.cvtColor(image_original, cv2.COLOR_BGR2GRAY)

# convertir a float32, requisito de la funcion cornerHarris()
image_gris_float = np.float32(image_gray)

# detectar los keypoints y calcular sus descriptores
# - blockSize: tamaño del vecindario considerado para detectar esquinas
# - ksize: tamaño del filtro Sobel usado en la aproximación del gradiente
# - k: parámetro libre usado en la ecuación de Harris (típicamente 0.04-0.06)
harris_detector = cv2.cornerHarris(image_gris_float, blockSize=2, ksize=3, k=0.04)

# aplicar una dilatación de la respuesta para resaltar mejor las esquinas
harris_dilate = cv2.dilate(harris_detector, None)

# umbral para considerar un punto como esquina
threshold = 0.01 * harris_dilate.max()

# donde la respuesta sea mayor al umbral, pintar de color verde
image_processed = image_original.copy()
image_processed[harris_dilate > threshold] = [0, 255, 0]

# mostrar la imagen original y la imagen procesada
cv2.imshow('Imagen original', image_original)
cv2.imshow('Esquinas detectadas (Harris)', image_processed)
cv2.waitKey(0)
cv2.destroyAllWindows()
