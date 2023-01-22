import numpy as np
import matplotlib.pyplot as plt
import cv2


grayscale_img = r'data\albert-einstein_gray.jpg'
colorscale_img = r'data\rgb-01.jpg'

# reading images
image_gray = cv2.imread(grayscale_img, cv2.IMREAD_GRAYSCALE)
image_color = cv2.imread(colorscale_img)

# showing images with opencv
plt.imshow(image_gray, cmap='gray')
# plt.show()
plt.imshow(image_color[:, :, ::-1])
# plt.show()

# scaling images
gray_resized = cv2.resize(src=image_gray, fx=2, fy=0.5, dsize=None)
plt.imshow(gray_resized, cmap='gray')
plt.show()

color_resized = cv2.resize(src=image_color, fx=1.3, fy=0.8, dsize=None)
plt.imshow(color_resized[:, :, ::-1])
plt.show()

