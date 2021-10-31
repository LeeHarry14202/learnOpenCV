from .__init__ import *

def rescaleFrame(frame, scale=0.75):
	width = int(frame.shape[1]*scale)
	height = int(frame.shape[0]*scale)
	dimensions = (width, height)
	return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def cropFrame(frame, y_start, y_stop, x_start, x_stop):
	return frame[y_start:y_stop,x_start:x_stop]


def changeRes(capture, width, height):
	capture.set(3, width)
	capture.set(4, height)
	capture.set(10, 100)
	return capture

def pytago(point):
	a = point[0]
	b = point[1]
	return int(sqrt(a**2 + b**2))

def warpImg(obj, img, width, height):
	pts1 = np.float32((obj.left_top, obj.right_top, obj.left_buttom, obj.right_buttom))
	pts2 = np.float32(([0, 0],[width,0],[0, height],[width, height]))
	matrix = cv.getPerspectiveTransform(pts1, pts2)
	imgOutput = cv.warpPerspective(img, matrix,(width,height))

	return imgOutput
