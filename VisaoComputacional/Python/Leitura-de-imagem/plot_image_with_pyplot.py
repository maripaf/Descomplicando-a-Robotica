# import
import cv2 as cv
from matplotlib import pyplot as plot

# read image
image = cv.imread('logo_color.png')

# converts BGR to RGB
image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)

# show image with pyplot
plot.imshow(image_rgb)
plot.show()

# wait with open window
cv.waitKey(0)
# destroy window
cv.destroyAllWindows()

