import cv2
import numpy as mp
import matplotlib.pyplot as plt
import numpy as np
import cv2


# 手动实现

def harris_corner_detection_with_nms(image, k=0.04, window_size=3, threshold=0.01, nms_window_size=5):
    #计算图像的梯度
    dx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    dy = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    #矩阵 M
    Ixx = dx * dx
    Iyy = dy * dy
    Ixy = dx * dy
    #M矩阵进行局部加权平均
    kernel = np.ones((window_size, window_size), np.float32) / (window_size**2)
    Ixx = cv2.filter2D(Ixx, -1, kernel)
    Iyy = cv2.filter2D(Iyy, -1, kernel)
    Ixy = cv2.filter2D(Ixy, -1, kernel)
    #角点响应函数
    det_M = Ixx * Iyy - Ixy**2
    trace_M = Ixx + Iyy
    harris_response = det_M - k * (trace_M**2)
    #应用阈值，找到角点
    corners = np.zeros_like(image)
    corners[harris_response > threshold * harris_response.max()] = 255
    #非极大值抑制 (NMS)
    corners = non_max_suppression(corners, nms_window_size)

    return corners

def non_max_suppression(corners, window_size):
    h, w = corners.shape

    half_window = window_size // 2
    new_corners = np.zeros_like(corners)

    for y in range(half_window, h - half_window):
        for x in range(half_window, w - half_window):
            window = corners[y - half_window:y + half_window + 1, x - half_window:x + half_window + 1]

            if corners[y, x] == np.max(window):
                new_corners[y, x] = corners[y, x]

    return new_corners

image = cv2.imread("chessboard.jpeg", 0)

blur_image=cv2.GaussianBlur(image,(3,3),0.1)
# 调用 Harris 角点检测函数
corners = harris_corner_detection_with_nms(blur_image)

# 显示角点
cv2.imshow("Harris Corners with NMS", corners)
cv2.waitKey(0)
cv2.destroyAllWindows()





# 直接调用opencv函数进行角点检测

image = cv2.imread("chessboard.jpeg", 0)

block_size= 2 # 角点检测的窗口大小
ksize = 3       # Sobel 导数的孔径大小
k = 0.04        # Harris 角点检测参数
threshold = 0.01  # 阈值，用于筛选角点

# 计算角点
harris_response = cv2.cornerHarris(image, blockSize=block_size, ksize=ksize, k=k)

# 执行非极大值抑制 (NMS)
harris_response = cv2.dilate(harris_response, None)  # 膨胀操作
image[harris_response > threshold * harris_response.max()] =255

plt.imshow(image)
plt.show()


