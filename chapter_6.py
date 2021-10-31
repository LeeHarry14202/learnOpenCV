from utils import *

img = cv.imread(lenaImg)

imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))

cv.imshow('Image Ver', imgVer)
cv.imshow('Image Hor', imgHor)

cv.waitKey(0)