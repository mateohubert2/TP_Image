import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('imagesTP/confiserie-smarties-lentilles_121-50838.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.figure()
plt.subplot(2,2,1)
plt.imshow(image)
plt.axis("off")
plt.title("Image RGB")

image_hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

hue, saturation, value = cv2.split(image_hsv)

plt.subplot(2,2,2)
plt.imshow(hue, cmap="hsv")
plt.axis("off")
plt.title("Teinte")

plt.subplot(2,2,3)
plt.imshow(saturation, cmap='gray')
plt.axis("off")
plt.title("Saturation")

plt.subplot(2,2,4)
plt.imshow(value, cmap='gray')
plt.axis("off")
plt.title("Luminosité")

plt.show()