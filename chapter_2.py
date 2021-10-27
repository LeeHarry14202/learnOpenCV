from utils import *

path = lenaImg

img = cv.imread(path)

imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# (7,7) is kernel how many blur do you want
# kernel is a odd number
kernel_size = (7,7)
imgBlur_1 = cv.GaussianBlur(img, kernel_size, 0)

kernel_size = (3,3)
imgBlur_2 = cv.GaussianBlur(img, kernel_size, 0)

imgCanny_1 = cv.Canny(img, 100, 100)
imgCanny_2 = cv.Canny(img, 150, 200)

kernel = np.ones((5,5), dtype=np.uint8)
imgDialation_1 = cv.dilate(imgCanny_1, kernel, iterations=1)
imgDialation_2 = cv.dilate(imgCanny_1, kernel, iterations=5)

imgEroded = cv.erode(imgDialation_1, kernel, iterations=1)

#cv.imshow('Image', img)
#cv.imshow('Gray Image', imgGray)
#cv.imshow('Blur Image 1', imgBlur_1)
#cv.imshow('Blur Image 2', imgBlur_2)
#cv.imshow('Canny Image 1', imgCanny_1)
#cv.imshow('Canny Image 2', imgCanny_2)
#cv.imshow('Dialation Image 1', imgDialation_1)
#cv.imshow('Dialation Image 2', imgDialation_2)
cv.imshow('Erode Image', imgEroded)

cv.waitKey(0)