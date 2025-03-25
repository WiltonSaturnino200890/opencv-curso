#Como dividir e fundir canais de cor no OpenCv;
#O OpenCV permite dividir uma imagem nos seus respectivos canais de cor. Depois pode pegar uma imagem RGB e dividi-la em componentes azul, verde e vermelho.


import cv2 as cv
import numpy as np

img = cv.imread('Photos/salvador.jpg')
cv.imshow('Salvador', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank,r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)
cv.waitKey(0)
