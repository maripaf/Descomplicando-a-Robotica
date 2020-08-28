# import
import cv2 as cv

# face classifier
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
# eye classifier
eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')
# cat classifier (used here as dog)
dog_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalcatface.xml')

# read image
image = cv.imread('zara_and_me.jpg')

# convert to gray scale
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# detect faces, eyes, and dog
faces = face_cascade.detectMultiScale(image_gray, 1.4, 5)
eyes = eye_cascade.detectMultiScale(image_gray, 1.3, 3)
dog = dog_cascade.detectMultiScale(image_gray, 1.3, 3)

# draw retangle in faces
for (x, y, w, h) in faces:
    cv.rectangle(image, (x, y), (x+w, y+h), (255,100,100), 2)
    cv.putText(image, 'face', (x, y-5), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 100, 100), 2, cv.LINE_AA)

# draw retangle in eyes
for (x, y, w, h) in eyes:
    cv.rectangle(image, (x, y), (x+w, y+h), (0,255,0), 2)
    cv.putText(image, 'eye', (x, y-5), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv.LINE_AA)

# draw retangle in dog face
for (x, y, w, h) in dog:
    cv.rectangle(image, (x, y), (x+w, y+h), (0,255,255), 2)
    cv.putText(image, 'dog', (x, y-5), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv.LINE_AA)
        
# display the output
cv.imshow('face_recognition', image)
cv.waitKey()
