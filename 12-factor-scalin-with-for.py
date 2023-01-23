import numpy as np
import matplotlib.pyplot as plt
import cv2


def f_bilinear_interpolation(x, y, I):

    left_col = int(y)
    right_col = left_col + 1
    top_row = int(x)
    bottom_row = top_row + 1

    right_weight = y - left_col
    left_weight = right_col - y
    top_weight = bottom_row - x
    bottom_weight = x - top_row

    if top_row>=0 and bottom_row<I.shape[0] and left_col>=0 and right_col<I.shape[1]:
        up = left_weight*(I[top_row, left_col]) + right_weight*(I[top_row, right_col])
        down = left_weight*(I[bottom_row, left_col]) + right_weight*(I[bottom_row, right_col])
        g = top_weight*(down) + bottom_weight*(up)
        return np.uint8(g)
    else:
        return 0


def f_scale_image(S, image):
    rows = (image.shape[0]) * S[0, 0]
    cols = (image.shape[1]) * S[1, 1]
    image_2 = np.zeros((rows, cols), dtype=np.uint8)
    Tinv = np.linalg.inv(S)
    for new_x in range(rows):
        for new_y in range(cols):
            p_dash = np.array([new_x, new_y])
            P = Tinv.dot(p_dash)
            x, y = P[0], P[1]
            if x < 0 or x >= image.shape[0] or y < 0 or y >= image.shape[1]:
                pass
            else:
                g = f_bilinear_interpolation(x, y, image)
                image_2[new_x, new_y] = g
    return image_2


fx = 4
fy = 3
S = np.array([[fx, 0], [0, fy]])
grayscale_img = r'data\albert-einstein_gray.jpg'
image = cv2.imread(grayscale_img, cv2.IMREAD_GRAYSCALE)
img = f_scale_image(S, image)

plt.imshow(img, cmap='gray')
plt.show()
