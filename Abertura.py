import cv2
import numpy as np
import matplotlib.pyplot as plt
from TransformaImagem import TransformaImagem

lena = cv2.imread('lena.jpg', 0)
imgbinaria=[]

for l in range(len(lena)):
    linha=[]
    for c in range(len(lena[0])):
        if(lena[l][c]>=126):
            linha.append(1)
        else:
            linha.append(0)
    imgbinaria.append(linha)

transforma = TransformaImagem()
imagemResultante = transforma.erosão(imgbinaria)
imagemResultante2 = transforma.dilatação(imagemResultante)

print("Matriz Original")
print(np.matrix(lena))
print()
print("Matriz Resultante")
print(np.matrix(imagemResultante))


plt.subplot(1,4,1), plt.imshow(lena,"gray", vmin=0, vmax=255), plt.title('Imagem Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,4,2), plt.imshow(imgbinaria,"gray", vmin=0, vmax=1), plt.title('Imagem Binária'), plt.xticks([]), plt.yticks([])
plt.subplot(1,4,3), plt.imshow(imagemResultante,"gray", vmin=0, vmax=1), plt.title('Imagem Resultante Erosão'), plt.xticks([]), plt.yticks([])
plt.subplot(1,4,4), plt.imshow(imagemResultante2,"gray", vmin=0, vmax=1), plt.title('Imagem Resultante Abertura'), plt.xticks([]), plt.yticks([])
plt.show()
