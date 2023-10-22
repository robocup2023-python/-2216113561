# 1

# def calculate(*args):
#     sum=0
#     count=0
#     for i in args:
#         sum+=i
#         count+=1
#     ava=sum/count
#     tup=(ava,)
#     for i in args:
#         if i>ava:
#             tup+=(args.index(i),)
#     return tup

# print(calculate(1,2,3,4,5,6))



# 2

# def odd(list):
#     odd_list=[]
#     for i in range(1,len(list),2):
#         odd_list.append(list[i])
#     return odd_list
# print(odd([0,1,2,3,4,5,6,7,8,9]))



# 3
# for i in range(1, 101):
#     file_name = f"file{i}.txt"
#     with open(file_name, "w") as file:
#         file.write(f"This is file {i}")



# 4
# import os
# import random

# # 获取当前目录下的所有文件名
# file_names = os.listdir()
# # 随机选择50个文件进行改名
# selected_files = random.sample(file_names, 50)
# for file_name in selected_files:
#     # 获取文件的扩展名
#     _, ext = os.path.splitext(file_name)
#     # 如果不是以.jpg结尾，则进行改名
#     if ext != ".jpg":
#         new_file_name = os.path.splitext(file_name)[0] + ".jpg"
#         os.rename(file_name, new_file_name)