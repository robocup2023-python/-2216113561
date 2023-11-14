import cv2
import numpy as np
from matplotlib import pyplot as plt


image = cv2.imread('musk.jpeg', 0)  # 以灰度模式读取图像

f_transform = np.fft.fft2(image)
f_transform_shifted = np.fft.fftshift(f_transform)  # 将低频移到图像中心

magnitude_spectrum = np.abs(f_transform_shifted)

# 创建掩膜，保留中心部分，将其它部分置为0
rows, cols = image.shape
center_row, center_col = rows // 2, cols // 2
mask_radius = 10  # 设定半径
mask = np.ones((rows, cols), np.uint8)
cv2.circle(mask, (center_col, center_row), mask_radius, 0, -1)

# 应用掩膜
f_transform_shifted_masked = f_transform_shifted * mask

# 进行反变换
f_inverse_shifted = np.fft.ifftshift(f_transform_shifted_masked)
image_restored = np.fft.ifft2(f_inverse_shifted).real

plt.figure()
plt.subplot(1,3,1)
plt.imshow(image, cmap='gray')
plt.title('Original')
plt.xticks([]), plt.yticks([])

(plt.subplot(1,3,2),
plt.imshow(np.log(1 + magnitude_spectrum), cmap='gray'))
plt.title('Masked')
plt.xticks([]), plt.yticks([])

plt.subplot(133)
plt.imshow(image_restored, cmap='gray')
plt.title('Restored')
plt.xticks([]), plt.yticks([])

plt.show()
