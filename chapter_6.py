from utils import *

img = cv.imread(lenaImg)
img_1 = cv.imread(lamboImg)

imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))

cv.imshow('Image Ver', rescaleFrame(imgVer, 0.5))
cv.imshow('Image Hor', rescaleFrame(imgHor, 0.5))

cv.waitKey(0)