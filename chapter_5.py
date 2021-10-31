import cv2.cv2

from utils import *

class CARD:
	def __init__(self,left_top, right_top, left_buttom,right_buttom):
		self.left_top = left_top
		self.right_top = right_top
		self.left_buttom = left_buttom
		self.right_buttom = right_buttom

	def getWidth(self):
		return pytago(self.left_top - self.right_top)

	def getHeight(self):
		return pytago(self.left_top - self.left_buttom)

path = cardsImg

img = cv.imread(path)

card_1 = CARD(left_top = np.array([110, 220]),
			right_top = np.array([290, 190]),
			left_buttom = np.array([155, 485]),
			right_buttom = np.array([355, 440]))

width = card_1.getWidth()
height = card_1.getHeight()

imgOutput_1 = warpImg(card_1, img, width, height)

cv.imshow('Image', img)
cv.imshow('imgOutput', imgOutput_1)

cv.waitKey(0)