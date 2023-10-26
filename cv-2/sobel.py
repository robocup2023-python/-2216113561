import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("einstein.jpeg", 0)

# 使用Sobel算子进行图像滤波
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

# 计算梯度幅度和方向
gradient_magnitude = np.sqrt(sobel_x**2 + sobel_y**2) #也可以取绝对值相加（更快）
gradient_direction = np.arctan2(sobel_y, sobel_x)

plt.figure(figsize=(24,12))
plt.subplot(131), plt.imshow(image, cmap='gray')
plt.title('origin'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(gradient_magnitude, cmap='gray')
plt.title('gradient_magnitude'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(gradient_direction, cmap='gray')
plt.title('gradient_direction'), plt.xticks([]), plt.yticks([])
plt.show()
