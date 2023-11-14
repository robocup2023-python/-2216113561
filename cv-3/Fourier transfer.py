import cv2
import matplotlib.pyplot as plt
import numpy as np


image = cv2.imread('edshreean.jpeg', 0)  # 以灰度模式读取图像
# 进行二维傅里叶变换
f_transform = np.fft.fft2(image)
f_transform_shifted = np.fft.fftshift(f_transform)  # 将低频移到图像中心

# 计算幅度谱和相位谱
magnitude_spectrum = np.abs(f_transform_shifted)
phase_spectrum = np.angle(f_transform_shifted)

# 显示原始图像和变换结果
plt.figure()
plt.subplot(1,3,1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.xticks([])
plt.yticks([])

plt.subplot(1,3,2)
plt.imshow(np.log(1 + magnitude_spectrum), cmap='gray')
plt.title('Magnitude Spectrum')
plt.xticks([])
plt.yticks([])

plt.subplot(1,3,3)
plt.imshow(phase_spectrum, cmap='gray')
plt.title('Phase Spectrum')
plt.xticks([])
plt.yticks([])

plt.show()


