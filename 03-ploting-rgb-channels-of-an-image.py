import numpy as np
import matplotlib.pyplot as plt

image = plt.imread(r'F:\computer-vision-area\practices\data\rgb-01.jpg')
im_copy = image.copy()

r = im_copy[:, :, 0]
g = im_copy[:, :, 1]
b = im_copy[:, :, 2]

plt.figure(1)

plt.subplot(221)
plt.imshow(im_copy)
plt.xticks([])
plt.yticks([])
plt.title('RGB')

plt.subplot(222)
plt.imshow(r, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('RED')

plt.subplot(223)
plt.imshow(g, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('GREEN')

plt.subplot(224)
plt.imshow(b, cmap='gray')
plt.xticks([])
plt.yticks([])
plt.title('Blue')

plt.show()
