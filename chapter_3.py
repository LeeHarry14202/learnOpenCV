from utils import *

path = lamboImg

img = cv.imread(path)
imgResize = rescaleFrame(img)
imgCropped = cropFrame(img, 0, 200, 200, 500)


print(img.shape)
print(imgResize.shape)
print(imgCropped.shape)

cv.imshow('Image', img)
cv.imshow('Image Rescaled', imgResize)
cv.imshow('Image Cropped', imgCropped)


cv.waitKey(0)