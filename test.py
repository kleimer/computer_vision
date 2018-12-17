import cv2 as cv
import numpy as np

hsv_min = np.array((0, 54, 5), np.uint8)
hsv_max = np.array((187, 255, 253), np.uint8)

image = cv.imread("opencv_original.jpeg")
#cv2.imshow("Original image", image)
#cv2.waitKey(0)
print(image.shape)
hsv=cv.cvtColor(image,cv.COLOR_BGR2HSV)
#thresh = cv.inRange( hsv, hsv_min, hsv_max )
cv.imshow("ttt",hsv)
cv.waitKey(0)