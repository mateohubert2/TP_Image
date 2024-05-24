import cv2
import numpy as np
from matplotlib import pyplot as plt

def hist(im):
    h = np.zeros((256))
    for p in im.ravel():
        h[p] += 1
    return h


def densite(h):
    s = 0
    res = np.zeros_like(h)
    for i in range(len(h)):
        res[i] = s
        s += h[i]
    return res/s

def egaliser(im):
    d_im = densite(hist(im))
    im_eq = np.zeros_like(im)
    for i in range(im.shape[0]):
        for j in range(im.shape[1]):
            im_eq[i,j] = np.round(d_im[im[i, j]] * 255)
    return im_eq

# Charger l'image en couleur
image = cv2.imread('imagesTP/rue.jpg')
histo_image = hist(image)
densite_image = densite(histo_image)
image_egalise = egaliser(image)

plt.figure()
plt.imshow(image)
plt.axis("off")
plt.title("Image originale")

plt.figure()
plt.plot(histo_image)
plt.plot(hist(image_egalise))
plt.title("Histogramme image originale (bleu), image égalisée (orange)")

plt.figure()
plt.plot(densite_image)
plt.title("Densité image originale")

plt.figure()
plt.axis("off")
plt.imshow(image_egalise, cmap = "gray");
plt.title("Image égalisée")

plt.figure()
plt.plot(densite(hist(image_egalise)))
plt.title("Densité image égalisée")

plt.show()