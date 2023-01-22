import numpy as np
import matplotlib.pyplot as plt

image = plt.imread(r'data\rgb-01.jpg')
im_copy = image.copy()

r = im_copy[:, :, 0]
r = r[:, :, np.newaxis]
g = im_copy[:, :, 1]
g = g[:, :, np.newaxis]
b = im_copy[:, :, 2]
b = b[:, :, np.newaxis]

bgr_img = np.concatenate((b, r, g), axis=2)

plt.figure(1)

plt.subplot(121)
plt.imshow(image)
plt.title('RGB')
plt.xticks([])
plt.yticks([])

plt.subplot(122)
plt.imshow(bgr_img)
plt.title('BGR')
plt.xticks([])
plt.yticks([])

plt.show()
