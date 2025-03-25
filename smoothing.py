import cv2 as cv

img = cv.imread('Photos/felicia.jpeg')
cv.imshow('Felicia', img)

# Average 
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)
#Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Media Blur', median)

#Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25) 
cv.imshow('Bilateral', bilateral)
cv.waitKey(0)