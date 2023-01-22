import cv2
import numpy as np

image = cv2.imread(r'data\rgb-01.jpg')
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# we choose a range of colors to extracting:
lr1 = np.array([0, 120, 70])
ur1 = np.array([15, 255, 255])
mask1 = cv2.inRange(hsv_image, lr1, ur1)

lr2 = np.array([165, 120, 70])
ur2 = np.array([180, 255, 255])
mask2 = cv2.inRange(hsv_image, lr2, ur2)

# in hsv map color, we have two part of red colors :)
mask = mask1 | mask2

result = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Red Roses", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
