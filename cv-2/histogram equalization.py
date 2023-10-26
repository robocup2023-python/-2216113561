import matplotlib.pyplot as plt
import numpy as np
import cv2

def histogram_equalization(image):
    # 获取图像的高度和宽度
    h, w = image.shape

    # 计算图像的直方图
    histogram = np.zeros(256, dtype=int)
    for i in range(h):
        for j in range(w):
            histogram[image[i, j]] += 1


    # 计算累积直方图，可以调用numpy库函数
    cumulative_histogram = np.cumsum(histogram)

    # 计算新的像素值（对每一个pixel）
    new_image = np.zeros((h, w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            new_pixel = int(((cumulative_histogram[image[i, j]]) / (h * w)) * 255)
            new_image[i, j] = new_pixel

    return new_image

image = cv2.imread("hq.jpeg", 0)

equalized_image = histogram_equalization(image)

plt.figure()

plt.subplot(1,2,1)
plt.imshow(image,cmap='gray')
plt.title("original")

plt.subplot(1,2,2)
plt.imshow(equalized_image,cmap='gray')
plt.title("after")
plt.show()