#1

# 用于指定变量、函数参数和返回值的类型的注释机制，
# 它并不影响程序的运行，但可以提供有关代码中数据类型的重要信息，
# 类型提示主要用于静态类型检查工具。

#2

import random
from typing import List, Tuple

def operatefile(name:str)->tuple:
    with open(name,'w') as file_object:
        for i in range(10):
            for j in range(3):
                num=random.randint(1,10) #生成一个随机数，并将其写入文件
                file_object.write(str(num))
                if j==0 or j==1:
                    file_object.write(",")
            file_object.write("\n")
    total=0
    ava:int=None
    mid:int=None
    list_sec_column:list[int]=[]
    list_sec_column_num:list[int]=[]
    with open(name) as file_object_2:
        datalist:list=file_object_2.readlines()
    for i in datalist:
        list_sec_column.append(i[2])
    for i in  list_sec_column:
        list_sec_column_num.append(int(i))
    list_sec_column_num.sort()
    max:int=list_sec_column_num[-1]
    min:int=list_sec_column_num[0]
    mid=(list_sec_column_num[4]+list_sec_column_num[5])/2
    for num in list_sec_column_num:
        total+=num
    ava=total/10
    return max,min,mid,ava #元祖打包，返回tuple类型
