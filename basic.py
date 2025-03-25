import cv2 as cv

img = cv.imread('Photos/felicia.jpeg')

cv.imshow('Felicia', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge  Cascate (Cascata de Borda)
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilacting  image
dilacted = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilacted)

# Eroding
eroded= cv.erode(dilacted, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

# Resized
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)
cv.waitKey(0)