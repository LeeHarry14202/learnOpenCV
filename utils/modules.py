import cv2 as cv

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

