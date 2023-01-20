import numpy as np
import matplotlib.pyplot as plt
import cv2

# this function shows how rgb converts to hsv:
# pixel by pixel
def f_rgb_to_hsv(r, g, b, scale_factor):
    r, g, b = r/255.0, g/255.0, b/255.0

    max_c = max(r, g, b)
    min_c = min(r, g, b)

    # calculating v
    v = max_c * scale_factor

    # calculating s
    if max_c == 0:
        s = 0
    else:
        s = ((max_c - min_c) / max_c) * scale_factor

    # calculating H
    diffr = max_c - min_c
    if max_c == min_c:
        h = 0
    elif max_c == r:
        h = (60 * ((g - b) / diffr) + 0) % 360
    elif max_c == g:
        h = (60 * ((b - r) / diffr) + 120) % 360
    elif max_c == b:
        h = (60 * ((r - g) / diffr) + 240) % 360
    if h < 0:
        h = h + 360

    return h, s, v

print(100, 200, 50, 100)

# but opencv does it for us easily
im = cv2.imread(r'F:\computer-vision-area\practices\data\rgb-01.jpg')

hsv_im = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv image", hsv_im)
cv2.waitKey(0)
cv2.destroyAllWindows()

