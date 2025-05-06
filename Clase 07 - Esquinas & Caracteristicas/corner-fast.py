import numpy as np
import cv2

# cargar la imagen y convertir a escala de grises
image_original = cv2.imread('../Recursos/goku.jpg')
image_gray = cv2.cvtColor(image_original, cv2.COLOR_BGR2GRAY)

# crear el detector de esquinas FAST
# - threshold: umbral para la detección de esquinas
fast_detector = cv2.FastFeatureDetector_create(threshold=50, nonmaxSuppression=True)

# detectar los keypoints
keypoints = fast_detector.detect(image_gray, None)

# pintar de color verde las esquinas detectadas
image_processed = cv2.drawKeypoints(image_original, keypoints, None, color=(0, 255, 0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# mostrar la imagen original y la imagen procesada
cv2.imshow('Imagen original', image_original)
cv2.imshow('Esquinas detectadas (FAST)', image_processed)
cv2.waitKey(0)
cv2.destroyAllWindows()
