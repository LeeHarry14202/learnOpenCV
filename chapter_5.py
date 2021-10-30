from utils import *

path = cardsImg

img = cv.imread(path)

cv.imshow('Image', img)

cv.waitKey(0)