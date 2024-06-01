import numpy as np

from matplotlib import pyplot as plt
import cv2
from mpl_toolkits import mplot3d

def affiche_image(img):
    plt.figure()
    plt.imshow(img,cmap="gray")
    plt.colorbar()

def  atom(n,m,fx,fy):
    img=np.zeros((n, m))
    x = np.array(np.arange(0,m))
    y = np.arange(0,n)
    e1 = np.exp(1j*2*np.pi*fx*x)
    e2 = np.exp(1j*2*np.pi*fy*y)
    for i in range(n):
        for j in range(m):
            img[i,j] = np.real(e2[i]*np.conjugate(e1[j]))
    return img

def fourier2d(img,fe):
    #Récupère la hauteur de l'image dans height et la largeur dans witdh
    [height, width] =img.shape
    #Fait la TF à 2 dimensions sur l'image et rassemble les zéros
    #au milieu au centre du spectre
    f = np.abs(np.fft.fftshift(np.fft.fft2(img)))
    #n prend comme valeur la largeur de l'image / 2
    n = width/2
    #m prend comme valeur la hauteur de l'imgae / 2
    m = height/2
    #Ouvre une figure
    plt.figure()
    #Paramètre l'affiche en 3 dimensions
    ax = plt.axes(projection='3d')
    #Paramètre l'axe x du graphique de -0.5 à 0.5 avec un pas de fe/width
    x = np.arange(-n/width, n/width, float(fe/width))
    #Même chose pour l'axe y
    y = np.arange(-m/height, m/height, float(fe/height))
    #Utilise les deux vecteurs précédents pour créer une matrice
    #X recupère une matrice générée via x et Y une matrice générée via -y
    X, Y = np.meshgrid(x, -y)
    #Affiche la taille de la matrice contenue dans X
    print(X.shape)
    #Remplit le graphique 3D en utilisant la matrice X, Y et la FFT
    ax.plot_surface(X, Y, np.sqrt(f))
    #Intitulation du graphique et des axes
    plt.title("Spectre 2D")
    plt.xlabel("Fx")
    plt.ylabel("Fy")
    #Ouvre une nouvelle figure
    plt.figure()
    #Affiche la TD en à "plat"
    plt.imshow(np.log(5*f+1),extent=[-n/width, n/width, -m/height, m/height])
    plt.colorbar()
    plt.xlabel("Fx")
    plt.ylabel("Fy")
    plt.title("Spectre 1D")


if __name__ == "__main__":
    #plt.figure()
    #img=atom(128, 128, 0.15, 0.37)
    #plt.imshow(img)
    #fourier2d(img, 1)
    plt.figure()
    img=atom(128, 128, 0.15, 0.37)[0::2]
    plt.imshow(img)
    fourier2d(img, 1)
    plt.show()