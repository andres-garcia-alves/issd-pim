import numpy as np
import cv2

# cargar la imagen y convertir a escala de grises
image_original = cv2.imread('../Recursos/goku.jpg')
image_gray = cv2.cvtColor(image_original, cv2.COLOR_BGR2GRAY)

# crear el detector de esquinas SIFT
sift = cv2.SIFT_create(contrastThreshold=0.12)
# sift = cv2.SIFT_create(contrastThreshold=0.04, edgeThreshold=10, sigma=1.6)

# detectar los keypoints y calcular sus descriptores
keypoints, descriptors = sift.detectAndCompute(image_gray, None)

# pintar de color verde las esquinas detectadas
image_processed = cv2.drawKeypoints(
    image_original,
    keypoints,
    None,
    flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
    color=(0, 255, 0)
)

# mostrar la imagen original y la imagen procesada
cv2.imshow('Imagen original', image_original)
cv2.imshow('Esquinas detectadas (SIFT)', image_processed)
cv2.waitKey(0)
cv2.destroyAllWindows()

# imprimir información sobre los puntos clave y descriptores
print("Número de puntos clave detectados:", len(keypoints))
print("Tamaño de los descriptores:", descriptors.shape if descriptors is not None else "N/A")
print("-------")
print("Primer descriptor:", descriptors[0] if descriptors is not None else "N/A")
print("Primer punto clave:", keypoints[0].pt if keypoints else "N/A")
print("Primer punto clave (tamaño):", keypoints[0].size if keypoints else "N/A")
print("Primer punto clave (ángulo):", keypoints[0].angle if keypoints else "N/A")
print("Primer punto clave (respuesta):", keypoints[0].response if keypoints else "N/A")
print("Primer punto clave (octavas):", keypoints[0].octave if keypoints else "N/A")
print("Primer punto clave (class_id):", keypoints[0].class_id if keypoints else "N/A")
