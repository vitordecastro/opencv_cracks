# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 19:39:17 2023

@author: Vitor e Vagner
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

# Carrega imagens
img = cv2.imread('./crack1.jpg')
img2 = cv2.imread('./crack2.jpg')
img3 = cv2.imread('./crack3.jpg')
img4 = cv2.imread('./crack4.jpg')

# Converte em escala de cinza
im_gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# im_gray_image2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# im_gray_image3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
# im_gray_image4 = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)

# Métodos para Binarizar
ret1, th1 = cv2.threshold(im_gray_image, 100, 255, cv2.THRESH_BINARY)
ret2,th2 = cv2.threshold(im_gray_image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
blur = cv2.GaussianBlur(im_gray_image, (1,5), 0)
ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# green
# img_green=th1.copy()
# img_green[th1==255]=(0,255,0)

titles = ['Original Image',
          'Gray Scale',
          'Global Thresholding (v = 100)',
          'Thresholding',
          'Gaussian Thresholding']
images = [img, im_gray_image, th1, th2, th3]

# Mostra com pyplot
for i in range(len(images)):
    plt.subplot(3, 3, i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

# Mostra com cv
# img_window_name = "image{number}"
# for i in range(len(images)):
#     cv2.imshow(img_window_name.format(number=i), images[i])

# Mantém janela aberta
plt.show()
# cv2.waitKey(0)
# cv2.destroyAllWindows()
