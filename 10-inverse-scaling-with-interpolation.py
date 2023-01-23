import numpy as np
import matplotlib.pyplot as plt
import cv2

S = np.array([[2, 0], [0, 2]])
grayscale_img = r'data\albert-einstein_gray.jpg'
image = cv2.imread(grayscale_img, cv2.IMREAD_GRAYSCALE)

rows = (image.shape[0])*2
cols = (image.shape[1])*2

image_2 = np.zeros((rows, cols), dtype=np.uint8)

Tinv = np.linalg.inv(S)
print(Tinv)

for new_x in range(rows):
    for new_y in range(cols):
        # p_dash is each pixel's coordinate [x, y]
        p_dash = np.array([new_x, new_y])
        # p is a coordinate in image 1 that may be a continuous coordinate
        P = Tinv.dot(p_dash)
        # that's why we need interpolation for finding right coordinate to use
        # in this code, we are using nearest neighbour
        # floor func can do this for us
        P = np.uint16(np.round(P))
        x, y = P[0], P[1]
        if x<0 or x>=image.shape[0] or y<0 or y>=image.shape[1]:
            pass
        else:
            image_2[new_x, new_y] = image[x, y]

plt.imshow(image_2, cmap='gray')
plt.show()
# we did it! but it takes much time :| (opencv can handel it for us)

