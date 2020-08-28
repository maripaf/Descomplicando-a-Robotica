import cv2 as cv

video = cv.VideoCapture(0)

while 1:
    ret, image = video.read()   
    cv.imshow('Video', image)
    if cv.waitKey(30) & 0xFF == ord('q'):
        break

video.release()
cv.destroyAllWindows()


