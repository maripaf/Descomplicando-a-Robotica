# import
import cv2 as cv

# read image in gray scale
image_gray = cv.imread('logo_color.png', 0)

# save image in gray scale in file
cv.imwrite('logo_gray.png', image_gray)


