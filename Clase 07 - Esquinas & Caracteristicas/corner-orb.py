import numpy as np
import cv2

# cargar la imagen y convertir a escala de grises
image_original = cv2.imread('../Recursos/goku.jpg')
image_gray = cv2.cvtColor(image_original, cv2.COLOR_BGR2GRAY)

# crear el detector ORB
orb = cv2.ORB_create(
    nfeatures=500,      # máximo número de keypoints a detectar
    scaleFactor=1.2,    # factor de escala entre niveles en la pirámide
    nlevels=8,          # número de niveles en la pirámide
    edgeThreshold=31,   # tamaño del margen de la imagen en el que no se detectan keypoints
    firstLevel=0,       # primer nivel de la pirámide (normalmente 0)
    WTA_K=2,            # número de puntos a comparar por BRIEF (2, 3, 4)
    scoreType=cv2.ORB_HARRIS_SCORE, #Método para puntuar la respuesta de corner (Harris o FAST)
    patchSize=25,       # tamaño del parche que se usa para la orientación BRIEF
    fastThreshold=20    # umbral para FAST (para detección inicial de esquinas)
)

# detectar los keypoints y calcular sus descriptores
keypoints, descriptores = orb.detectAndCompute(image_gray, None)

# dibujar los keypoints en la imagen original
imagen_con_keypoints = cv2.drawKeypoints(
    image_original,
    keypoints,
    None,
    color=(0, 255, 0),
    flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)

# mostrar resultados
cv2.imshow('Imagen Original', image_original)
cv2.imshow('ORB Keypoints', imagen_con_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()

# imprimir estadísticas
print(f"Se han detectado { len(keypoints) } keypoints.")
print(f"Dimensiones de los descriptores: { descriptores.shape }")
