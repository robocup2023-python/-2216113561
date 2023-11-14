import cv2
import numpy as np
from matplotlib import pyplot as plt


image1 = cv2.imread('edshreean.jpeg', 0)
image2 = cv2.imread('Justin.jpeg', 0)
# 尺寸
min_rows = min(image1.shape[0], image2.shape[0])
min_cols = min(image1.shape[1], image2.shape[1])
image1 = cv2.resize(image1, (min_cols, min_rows))
image2 = cv2.resize(image2, (min_cols, min_rows))

# 二维傅立叶变换
f_transform1 = np.fft.fft2(image1)
f_transform2 = np.fft.fft2(image2)

f_transform_shifted1 = np.fft.fftshift(f_transform1)
f_transform_shifted2 = np.fft.fftshift(f_transform2)

# 融合两幅图像的频谱
weight=0.5
f_transform_shifted_combined = weight * f_transform_shifted1 + (1 - weight) * f_transform_shifted2

#反变换
f_inverse_shifted_combined = np.fft.ifftshift(f_transform_shifted_combined)
image_combined = np.fft.ifft2(f_inverse_shifted_combined).real

plt.figure()
plt.subplot(1,3,1)
plt.imshow(image1, cmap='gray')
plt.title('ed')
plt.xticks([]), plt.yticks([])

plt.subplot(1,3,2)
plt.imshow(image2, cmap='gray')
(plt.title('justin'),
plt.xticks([]), plt.yticks([]))

plt.subplot(1,3,3)
plt.imshow(image_combined, cmap='gray')
plt.title("i don't care")
plt.xticks([]), plt.yticks([])

plt.show()
