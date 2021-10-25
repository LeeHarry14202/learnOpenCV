import cv2 as cv

path = './Resources/Photos/cat.jpg'

img = cv.imread(path)

cv.imshow('Cat', img)

cv.waitKey(0)
