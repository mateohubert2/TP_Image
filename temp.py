import cv2
import numpy as np
from matplotlib import pyplot as plt

# Lire l'image
image = cv2.imread('imagesTP/confiserie-smarties-lentilles_121-50838.jpg')

# Séparer les canaux R, G et B
B, G, R = cv2.split(image)

# Convertir les canaux en float pour éviter les problèmes de débordement dans les calculs
R = R.astype(np.float32)
G = G.astype(np.float32)
B = B.astype(np.float32)

# Calculer le numérateur et le dénominateur de l'expression
numerateur = R - (G / 2.0) - (B / 2.0)
denominateur = np.sqrt(R**2 + G**2 + B**2 - R*G - R*B - G*B)

# Ajouter une petite valeur epsilon pour éviter la division par zéro
epsilon = 1e-10
denominateur = np.clip(denominateur, epsilon, None)

# Calculer l'image Hp en appliquant la formule donnée
Hp = np.arccos(np.clip(numerateur / denominateur, -1, 1))

# Convertir Hp de radians en degrés
Hp_degrees = np.degrees(Hp)

# Créer l'image H
H = np.where(B > G, 360 - Hp_degrees, Hp_degrees)

# Normaliser les valeurs de l'image H pour qu'elles soient dans la plage [0, 255]
H_normalized = (H / 360) * 255.0
H_normalized = H_normalized.astype(np.uint8)

# Afficher l'image originale et la nouvelle image H
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.title("Image Originale")

plt.subplot(1, 2, 2)
plt.imshow(H_normalized, cmap='gray')
plt.axis("off")
plt.title("Nouvelle Image H")

plt.show()
