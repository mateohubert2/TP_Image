from math import acos, pi, sqrt
import cv2
import numpy as np
from matplotlib import pyplot as plt

def calculate_ihls(red_value: float, green_value: float, blue_value: float) -> tuple[float, float, float]:
    """
    Permet de calculer les valeurs 'hue', 'luminosity'
    :param red_value:
    :param green_value:
    :param blue_value:
    :return:
    """
    # Permet de calculer les différents canaux de
    # l'espace de couleur IHSL avec les formules du 
    # cours
    luminosity = float(0.2126 * red_value + 0.7152 * green_value + 0.0722 * blue_value)*255
    saturation = float(max(red_value, green_value, blue_value) - min(red_value, green_value, blue_value))*255
    hue = -1.0
    if red_value == green_value and green_value == blue_value:
        hue = 0.0
    else:
        denominator_value = (red_value ** 2) + (green_value ** 2) + (blue_value ** 2) - (red_value * green_value) - (red_value * blue_value) - (blue_value * green_value)
        total = ((red_value - (green_value / 2) - (blue_value / 2)) / (sqrt(denominator_value)))
        if total > 1:
            total = 1.0
        elif total < -1:
            total = -1.0
        hue = acos(total)
        hue = hue*(180/pi)
    if blue_value > green_value:
        hue = 360.0 - hue
    return hue, luminosity, saturation

def rgb2ihls(image):
  new_image = np.zeros_like(image)
  for i, j, color in np.ndindex(image.shape):
    colors = image[i][j]
    ihls_color = calculate_ihls(colors[0]/255.0, colors[1]/255.0, colors[2]/255.0)
    new_image[i][j] = list(ihls_color)
  return new_image

image = cv2.imread('imagesTP/confiserie-smarties-lentilles_121-50838.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
imageIHLS = rgb2ihls(image)

hue, luminosity, saturation = cv2.split(imageIHLS)

plt.figure()
plt.subplot(2,2,1)
plt.imshow(image)
plt.axis("off")
plt.title("Image RGB")

plt.subplot(2,2,2)
plt.imshow(hue, cmap="hsv")
plt.axis("off")
plt.title("Teinte")

plt.subplot(2,2,3)
plt.imshow(saturation, cmap='gray')
plt.axis("off")
plt.title("Saturation")

plt.subplot(2,2,4)
plt.imshow(luminosity, cmap='gray')
plt.axis("off")
plt.title("Luminosité")

plt.show()