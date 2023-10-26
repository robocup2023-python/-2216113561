import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread("einstein.jpeg",0)
blurred_image=cv2.GaussianBlur(image,(3,3),0.5)

#Sobel差分算子
sobel_x=cv2.Sobel(blurred_image,cv2.CV_64F,1,0,ksize=3)
sobel_y=cv2.Sobel(blurred_image,cv2.CV_64F,0,1,ksize=3)
gradient_mag=np.abs(sobel_x)+np.abs(sobel_y)
gradient_dir=np.arctan2(sobel_y,sobel_x)

#调用Canny库函数实现边缘检测
canny_image=cv2.Canny(blurred_image,70,80)

# 非最大抑制（NMS）
edges = cv2.dilate(canny_image, None)
edges = cv2.erode(edges, None)

# 边缘连接
link_image = cv2.bitwise_and(edges, edges, mask=None)

plt.subplot(2,3,1)
plt.imshow(gradient_mag, cmap='gray')
plt.title('Gradient Magnitude')
plt.xticks([]), plt.yticks([])

plt.subplot(2,3,2)
plt.imshow(gradient_dir, cmap='gray')
plt.title('Gradient Direction')
plt.xticks([]), plt.yticks([])

plt.subplot(2,3,3)
plt.imshow(canny_image, cmap='gray')
plt.title('Canny Image')
plt.xticks([]), plt.yticks([])

plt.subplot(2,3,4)
plt.imshow(edges, cmap='gray')
plt.title('NMS')
plt.xticks([]), plt.yticks([])

plt.subplot(2,3,5)
plt.imshow(link_image, cmap='gray')
plt.title('Edge_Link')
plt.xticks([]), plt.yticks([])

plt.show()





