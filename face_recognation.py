import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['Beyonce', 'Jay Z', 'Lebron James', 'Serena Williams', 'Will Smith']
#features = np.lead('features.npy', allow_pickles=True)
#labels = np.lead('lables.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.read('face_trained.yml')

img = cv.imread(r'C:\Users\wilto\Downloads\OpenCV\Faces\train\Jay Z\download (1).jpeg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+y, y+h), (0,255,0), thickness=2)

    cv.imshow('Detected face', img)

    cv.waitKey(0)