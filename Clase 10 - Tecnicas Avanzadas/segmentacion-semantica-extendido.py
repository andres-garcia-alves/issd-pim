import requests
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from transformers import SegformerForSemanticSegmentation, AutoImageProcessor
import torch
import matplotlib.patches as mpatches

# 1. cargar un modelo preentrenado en ADE20K (150 clases) por ejemplo:
model_name = "nvidia/segformer-b0-finetuned-ade-512-512"

processor = AutoImageProcessor.from_pretrained(model_name)
model = SegformerForSemanticSegmentation.from_pretrained(model_name)

# 2. cargar una imagen local en lugar de la URL
# asegúrate de que existe y sea similar a los datos de ADE20K (edificios, calles, interiores, etc.)
image_path = "../Recursos/avion-02.jpg"
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

# identificar las clases presentes en la segmentación
unique_classes = np.unique(pred)
print("Clases encontradas:", unique_classes)

# Lista de nombres de clases ADE20K (debe ser de longitud 150 en orden)
ade20k_classes = [
    "wall", "building", "sky", "floor", "tree", "ceiling", "road", "bed", "windowpane", "grass",
    "cabinet", "sidewalk", "person", "earth", "door", "table", "mountain", "plant", "curtain", "chair",
    "car", "water", "painting", "sofa", "shelf", "house", "sea", "mirror", "rug", "field",
    "armchair", "seat", "fence", "desk", "rock", "wardrobe", "lamp", "bathtub", "railing", "cushion",
    "base", "box", "column", "signboard", "chest of drawers", "counter", "sand", "sink", "skyscraper", "fireplace",
    "refrigerator", "grandstand", "path", "stairs", "runway", "case", "pool table", "pillow", "screen door", "stairway",
    "river", "bridge", "bookcase", "blind", "coffee table", "toilet", "flower", "book", "hill", "bench",
    "countertop", "stove", "palm", "kitchen island", "computer", "swivel chair", "boat", "bar", "arcade machine", "hovel",
    "bus", "towel", "light", "truck", "tower", "chandelier", "awning", "streetlight", "booth", "television receiver",
    "airplane", "dirt track", "apparel", "pole", "land", "bannister", "escalator", "ottoman", "bottle", "buffet",
    "poster", "stage", "van", "ship", "fountain", "conveyor belt", "canopy", "washer", "plaything", "swimming pool",
    "screen", "blanket", "sculpture", "hood", "sconce", "vase", "traffic light", "tray", "ashcan", "fan",
    "pier", "crt screen", "plate", "monitor", "bulletin board", "shower", "radiator", "glass", "clock", "flag"
]

# Crear leyenda con nombres y colores de las clases encontradas
legend_patches = []
for class_id in unique_classes:
    class_name = ade20k_classes[class_id] if class_id < len(ade20k_classes) else f"Clase {class_id}"
    color = colors[class_id] / 255  # Normaliza de 0-255 a 0-1 para matplotlib
    patch = mpatches.Patch(color=color, label=class_name)
    legend_patches.append(patch)

# 9. mostrar resultados con matplotlib (o lo guardamos en disco)
plt.figure(figsize=(15, 6))

plt.subplot(1, 2, 1)
plt.title("Imagen Original")
plt.imshow(image)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Segmentación Superpuesta")
plt.imshow(blended)
plt.axis("off")
plt.legend(handles=legend_patches, bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout()
plt.show()
