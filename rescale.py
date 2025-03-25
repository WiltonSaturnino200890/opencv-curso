import cv2 as cv

#img= cv.imread('Photos/felicia.jpeg')
#cv.imshow('felicia', img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

def changesRes(width, height):
   #Imagens, Vídeos and Live Vídeos
   capture.set(3, width)
   capture.read(4, height)
#Reading Vídeos
capture = cv.VideoCapture('Videos/lamber.mp4')

while True:
    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame, scale=.2)
    cv.imshow('Video', frame)
    cv.imshow('video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()