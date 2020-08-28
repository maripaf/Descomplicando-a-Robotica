# import
import cv2 as cv

# read image
image = cv.imread('logo_color.png')

# show image
cv.imshow('IMAGE', image)

# wait with open window
cv.waitKey(0)
# destroy window
cv.destroyAllWindows()


