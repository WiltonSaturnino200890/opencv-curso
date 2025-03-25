import cv2 as cv
"""
img= cv.imread('Photos/felicia.jpeg')

cv.imshow('felicia', img)
"""
#Reading Vídeos
capture = cv.VideoCapture('Videos/lamber.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()