import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage

image = cv2.imread('imagesTP/CerisierP.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

prewitt = ndimage.prewitt(image)
plt.figure()
plt.imshow(prewitt)
plt.show()