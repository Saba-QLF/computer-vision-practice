import numpy as np
import matplotlib.pyplot as plt
import cv2


grayscale_img = r'data\albert-einstein_gray.jpg'
image = cv2.imread(grayscale_img, cv2.IMREAD_GRAYSCALE)

rows = image.shape[0]
cols = image.shape[1]

image_2 = np.zeros((rows, cols), dtype=np.uint8)
plt.imshow(image_2, cmap='gray')
# plt.show()

# flipping with for loops

# vertically
for x in range(rows):
    for y in range(cols):
        x_2 = rows - x - 1
        image_2[x_2, y] = image[x, y]

plt.imshow(image_2, cmap='gray')
plt.show()

# horizontally
image_3 = image.copy()
for x in range(rows):
    for y in range(cols):
        y_2 = cols - y - 1
        image_3[x, y_2] = image[x, y]

plt.imshow(image_3, cmap='gray')
plt.show()

# cropping with for loops
image_4 = np.zeros((rows//2, cols), dtype=np.uint8)
for x in range(rows//2):
    for y in range(cols):
        image_4[x, y] = image[x, y]

plt.imshow(image_4, cmap='gray')
plt.show()