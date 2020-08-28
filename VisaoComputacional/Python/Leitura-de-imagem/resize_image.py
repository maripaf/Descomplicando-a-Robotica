# import
import cv2 as cv

# read image
image = cv.imread('logo_color.png')

# resize image
height = image.shape[0] #get height
width = image.shape[1] #get width
percent = 0.2
new_height = int(height * percent)
new_width = int(width * percent)

size = (new_height, new_width)

reduced_image = cv.resize(image, size, interpolation=cv.INTER_AREA)

# show image
cv.imshow('IMAGE', reduced_image)

# wait with open window
cv.waitKey(0)
# destroy window
cv.destroyAllWindows()



