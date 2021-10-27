from utils import *

img = np.zeros((512, 512,3), dtype=np.uint8)
# img[100:200, 100:200] = GREEN

width = img.shape[1]
height = img.shape[0]

x_mid = int(width / 2)
y_mid = int(height / 2)
mid_point = (x_mid, y_mid)

cv.line(img, (0,0), (width, height), RED,thickness = 2)
cv.line(img, (width,0), (0,height), RED, thickness = 2)

cv.line(img, (x_mid, 0), (x_mid, height), GREEN)
cv.line(img, (0, y_mid), (width, y_mid), GREEN)

cv.line(img, (0, y_mid), (x_mid,0), BLUE)
cv.line(img, (x_mid, 0), (width, y_mid), BLUE)
cv.line(img, (width, y_mid), (x_mid, height), BLUE)
cv.line(img, (x_mid, height), (0, y_mid), BLUE)

cv.rectangle(img,(int(x_mid /2),int(y_mid /2 )),(int(width * 3/4),int(height* 3/4)), WHITE, cv.FILLED)

cv.circle(img, (x_mid,y_mid), int(x_mid /2), RED, 2)

text = "OPENCV"
font = cv.FONT_HERSHEY_SIMPLEX

cv.putText(img, text,(mid_point), cv.FONT_HERSHEY_COMPLEX, 1,BLACK, 1)
cv.imshow('Image', img)
print(cv.getTextSize(text, font, 1, 2)[0])

cv.waitKey(0)
