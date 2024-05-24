import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage

image = cv2.imread("imagesTP/CerisierP.jpg")
blue,green,red = cv2.split(image)
derivX = cv2.Sobel(red,ddepth=-1,dx=1,dy=0)
derivY = cv2.Sobel(red,ddepth=-1,dx=0,dy=1)
gradient = derivX+derivY*1j
G = np.absolute(gradient)
plt.figure()
plt.imshow(G)
plt.show()