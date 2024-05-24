import cv2
import numpy as np
from matplotlib import pyplot as plt
# Charger l'image en couleur
image = cv2.imread('imagesTP/CerisierP.jpg')

# Convertir l'image en niveaux de gris
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Appliquer la méthode de binarisation d'Otsu
_, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_OTSU)

# Afficher les images
cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL) 
cv2.namedWindow("Binary Image", cv2.WINDOW_NORMAL) 

cv2.imshow("Original Image", image)
cv2.imshow("Binary Image", binary_image)

# Déplacer les fenêtres à des positions spécifiques
cv2.moveWindow("Original Image", 20, 100)
cv2.moveWindow("Binary Image", 1000, 100)

# Redimensionner les fenêtres à des tailles spécifiques
cv2.resizeWindow("Original Image", 900, 900)
cv2.resizeWindow("Binary Image", 900, 900)

cv2.waitKey(0)
cv2.destroyAllWindows()