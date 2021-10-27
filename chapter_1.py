from utils import *

# Reading Images
# path_1 = './Resources/Photqos/cat_large.jpg'
# path_2 = './Resources/Phqotos/cat.jpg'

# img = cv.imread(path_2)

# cv.imshow('Cat', img)

# cv.waitKey(0)

# Reading Videos
path = './Resources/Videos/dog.mp4'

capture = cv.VideoCapture(0)
capture = changeRes(capture, 500, 480)


while True:
	isTrue, frame = capture.read()

	resized_frame = rescaleFrame(frame, scale=0.2)

	cv.imshow('Video', frame)
	cv.imshow('Video resize', resized_frame)

	if cv.waitKey(1) & 0xFF==ord('q'):
		break

# capture.release()
# cv.destroyAllWindow()
