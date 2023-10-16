# 1

# import random
# file_name='text1.txt'
# with open(file_name,'w') as file_object:
#     for i in range(10):
#         for j in range(3):
#             num=random.randint(1,10) #生成一个随机数，并将其写入文件
#             file_object.write(str(num))
#             if j==0 or j==1:
#                 file_object.write(",")
#         file_object.write("\n")
# total=0
# ava=None
# mid=None
# list_sec_column=[]
# list_sec_column_num=[]
# with open(file_name) as file_object_2:
#     datalist=file_object_2.readlines()
# for i in datalist:
#     list_sec_column.append(i[2])
# for i in  list_sec_column:
#     list_sec_column_num.append(int(i))
# list_sec_column_num.sort()
# max=list_sec_column_num[-1]
# min=list_sec_column_num[0]
# mid=(list_sec_column_num[4]+list_sec_column_num[5])/2
# for num in list_sec_column_num:
#     total+=num
# ava=total/10
# print(max,min,ava,mid)



#2，3，4

# import random
# file_name="test2.txt"
# n=int(input("please input that how many lines you want the file has: "))
# with open(file_name,'w') as file_object:
#     for i in range(n):
#         ascii_char = chr(random.randrange(32, 127))
#         file_object.write(ascii_char)
#         if i != n-1:
#             file_object.write("\n")
# #复制
# file_name_2="copy_test2.txt"
# with open(file_name_2,'w') as file_object_copy,open(file_name) as file_object1:
#     for line in file_object1:
#         file_object_copy.write(line)
# # import shutil
# #开头追加（重写）
# with open(file_name,'r+') as file_object2:
#     content=file_object2.read()
#     file_object2.seek(0,0)
#     file_object2.write("python\n"+content)
# #结尾追加
# with open(file_name,'a') as file_object3:
#     file_object3.write("python\n")

# # 对比
# with open(file_name_2) as file_object_copy1,open(file_name) as file_object3:
#     i=1
#     for line1,line2 in zip(file_object3,file_object_copy1):
#         if line1 != line2:
#             print(i)
#         i+=1



# 5
# import os
# import random
# import string

# def create_files(directory, num_files, num_lines):
#     os.makedirs(directory, exist_ok=True)
#     for i in range(num_files):
#         filename = f"testfile_{i+1}.txt"
#         filepath = os.path.join(directory, filename)
#         with open(filepath, 'w') as file:
#             for _ in range(num_lines):
#                 random_text = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(1, 10)))
#                 file.write(random_text + '\n')
# 追加python修改
# def traverse_files(directory):
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             if file.endswith(".txt"):
#                 filepath = os.path.join(root, file)
#                 with open(filepath, 'r') as file:
#                     print(f"Filename: {file.name}-python")
#                     for line in file:
#                         print(line.rstrip() + "-python")

# def change_files(directory):
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             if file.endswith(".txt"):
#                 filepath = os.path.join(root, file)
#                 with open(filepath, 'r') as file:
#                     content = file.read()
#                     if "python" in file.name or "python" in content:
#                         new_content = content.replace("python", "class")
#                         with open(filepath, 'w') as file:
#                             file.write(new_content)

# i=int(input("please input i:"))
# j=int(input("please input j:"))


# test_directory = "test"
# create_files(test_directory, i, j)
# traverse_files(test_directory)
# change_files(test_directory)

    




            



    




