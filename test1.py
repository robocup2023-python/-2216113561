import cv2
import numpy as np
import matplotlib.pyplot as plt
def Gauss(x,y,s):#返回高斯函数的值
    pi=np.pi
    return ((1/(2*pi*(s**2)))*np.exp(-(x**2+y**2)/(2*(s**2))))

n=int(input("please input the dimension:"))
cigama=float(input("please input the variance:"))

# 创建高斯滤波核
gauss_filter=np.zeros((n,n),dtype="float32")
center=n//2
total=0
for x in range(-center,center+1):
    for y in range(-center,center+1):
        gauss_filter[x+center,y+center]=Gauss(x,y,cigama)
        total+=Gauss(x,y,cigama)
gauss_filter/=total
print("------")
print("my gauss kernel:")
print(gauss_filter)

# 利用cv库创建高斯滤波核
gauss_kernel_1=cv2.getGaussianKernel(n,cigama)
gauss_kernel_2=np.outer(gauss_kernel_1,gauss_kernel_1) #外积操作生成2维的高斯滤波核
print("-------")
print("cv's gauss kernel:")
print(gauss_kernel_2)

print("------")
print("\033[91mthe result is the same.\033[0m")

# # 可视化展示高斯滤波核
x1=np.linspace(-center,center,50)
y1=np.linspace(-center,center,50)
X1,Y1=np.meshgrid(x1,y1)
Z=Gauss(X1,Y1,cigama)
plt.contourf(X1,Y1,Z,levels=20,cmap='viridis')
plt.colorbar()
plt.xlabel('X')
plt.ylabel('Y')
plt.title("visual Guass Filter kernel ")
plt.show()

# 手动实现图像的卷积操作
image=cv2.imread("elonmusk.jpeg",cv2.IMREAD_COLOR)
height,width,channels=image.shape #元祖打包
blurred_image = np.zeros_like(image)
output_image=np.zeros_like(image)
for c in range(channels):
    for i in range(center,height-center):
        for j in range(center,width-center):
            #从原始图像中提取出一个与滤波核大小相同的图像块
            patch=image[i-center:i+center+1,j-center:j+center+1,c]
            if patch.shape[0]==n and patch.shape[1]==n:
                blurred_image[i,j,c]=np.sum(patch * gauss_kernel_2)  #图像与滤波核进行卷积
                # output_image[i, j, c] = np.clip(blurred_image, 0, 255)  # 将结果截断到 [0, 255] 范围内
cv2.imshow('original image',image)
cv2.imshow('after convolution',output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 利用cv库实现卷积操作
kernel_size=(n,n)
test_image=cv2.GaussianBlur(image,kernel_size,cigama)
cv2.imshow('Convolved Image', test_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 纯黑图像边界padding
image = cv2.imread("elonmusk.jpeg", cv2.IMREAD_COLOR)
# 定义要添加的填充像素数
padding_size = 2000
height, width, channels = image.shape
# 创建一个新的大图像，填充像素值为零
padded_image = np.zeros((height + 2 * padding_size, width + 2 * padding_size, channels), dtype=np.uint8)
# 将原始图像放入新图像中，中心对齐
padded_image[padding_size:height + padding_size, padding_size:width + padding_size] = image

cv2.imshow('Original Image', image)
cv2.imshow('Zero Padded Image', padded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 边缘复制padding
padding_size = 100
height, width, channels = image.shape
# 创建一个新的大图像，填充像素值为边缘像素值
padded_image = np.copy(image)
# 复制图像边缘像素值到填充区域 - 上边界
for i in range(padding_size):
    padded_image[i, :, :] = image[0, :, :]
# 复制图像边缘像素值到填充区域 - 下边界
for i in range(height + padding_size, height):
    padded_image[i, :, :] = image[height - 1, :, :]
# 复制图像边缘像素值到填充区域 - 左边界
for i in range(padding_size):
    padded_image[:, i, :] = image[:, 0, :]
# 复制图像边缘像素值到填充区域 - 右边界
for i in range(width + padding_size, width):
    padded_image[:, i, :] = image[:, width - 1, :]
cv2.imshow('Original Image', image)
cv2.imshow('Edge-Copy Padded Image', padded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()