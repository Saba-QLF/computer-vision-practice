import numpy as np
import matplotlib.pyplot as plt
import cv2

# Part 1
im = np.arange(1000)
print(im.shape)

# add axis in 0th pos and make our img 2d
im = im[np.newaxis, :]
print(im.shape)

# repeat our array n time in axis 0
im = np.repeat(im, 1000, axis=0)

plt.imshow(im, cmap='gray')
plt.show()

print('---------------------------------')

# Part 2
image = plt.imread(r'data\albert-einstein_gray.jpg')
# some images are read-only
image_copy = image.copy()
print(image_copy.shape)
print(image_copy.dtype)
plt.imshow(image_copy, cmap='gray')
plt.show()


image_copy[800:, :] = 0
plt.imshow(image_copy, cmap='gray')
plt.show()

# Saving an image
plt.imsave(r'F:\computer-vision-area\practices\data\albert-einstein_gray-02.jpg',
           image_copy, cmap='gray')

