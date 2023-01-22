import numpy as np
import matplotlib.pyplot as plt

image = plt.imread(r'data\albert-einstein_gray.jpg')
im_copy = image.copy()
plt.imshow(im_copy, cmap='gray')
plt.show()

im_copy[330:430, 300:400] = 69
im_copy[330:430, 440:540] = 69
plt.imshow(im_copy, cmap='gray')
plt.show()
plt.imsave(r'data\poor-einstein.jpg',
           im_copy, cmap='gray')