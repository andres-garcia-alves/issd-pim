import requests
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from transformers import SegformerForSemanticSegmentation, AutoImageProcessor
import torch

# 1. cargar un modelo preentrenado en ADE20K (150 clases) por ejemplo:
model_name = "nvidia/segformer-b0-finetuned-ade-512-512"

processor = AutoImageProcessor.from_pretrained(model_name)
model = SegformerForSemanticSegmentation.from_pretrained(model_name)

# 2. cargar una imagen local en lugar de la URL
# asegúrate de que existe y sea similar a los datos de ADE20K (edificios, calles, interiores, etc.)
image_path = "../Recursos/avion-01.jpg"
image = Image.open(image_path).convert("RGB")

# 3. preprocesar la imagen con el procesador del modelo
inputs = processor(images=image, return_tensors="pt")

# 4. realiza la predicción
with torch.no_grad():
  outputs = model(**inputs)

# la salida es un tensor de forma [batch_size, num_classes, height, width]
logits = outputs.logits

# (height, width) con valores de 0..num_classes-1
pred = torch.argmax(logits.squeeze(), dim=0).cpu().numpy()

# 5. creamos una paleta de colores para cada clase
# si el modelo está entrenado en ADE20K, normalmente hay 150 clases
num_classes = model.config.num_labels
print(num_classes)

# generamos una paleta aleatoria, o puedes definirla si conoces la palette del dataset
colors = np.random.randint(0, 255, size=(num_classes, 3), dtype=np.uint8)

# 6. convertimos la imagen segmentada a un mapa de colores
segmentation_map = np.zeros((pred.shape[0], pred.shape[1], 3), dtype=np.uint8)
for class_id in range(num_classes):
  segmentation_map[pred == class_id] = colors[class_id]

# 7. convertimos a PIL
segmentation_map_pil = Image.fromarray(segmentation_map)

# 8. superponemos el mapa de colores sobre la imagen original (del mismo tamaño)
segmentation_map_pil = segmentation_map_pil.resize(image.size)
blended = Image.blend(image, segmentation_map_pil, alpha=0.5)

# 9. mostrar resultados con matplotlib (o lo guardamos en disco)
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Imagen Original")
plt.imshow(image)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Segmentación Superpuesta")
plt.imshow(blended)
plt.axis("off")

plt.show()
