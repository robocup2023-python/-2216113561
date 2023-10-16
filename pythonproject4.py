# 1
# list=[1,2,3,4,5]
# strlist=str(list)
# result_list=" ".join(strlist)
# for i in result_list:
#     print(i,end='')



#2
# list=[1,2,3,4,5,6,7,9,10]
# insertnum=int(input("please input the insert number: "))
# if(insertnum>=list[-1]):
#     list.append(insert)
# elif(insertnum>=list[len(list)//2]):
#     for i in range(len(list)//2,len(list)-1):
#         if(insertnum<=list[i]):
#             list.insert(i,insertnum)
# elif(insertnum<list[len(list)//2]):
#     for i in range(0,len(list)//2):
#         if(list[i]>=insertnum):
#             list.insert(i,insertnum)

# print(list)


#3
# matrix1=[[12,7,3],
#          [4,5,6],
#          [7,8,9]]
# matrix2=[[5,8,1],
#          [6,7,3],
#          [4,5,9]]

# resultmatrix=[[0,0,0],
#               [0,0,0],
#               [0,0,0]]
# for i in range(len(matrix1)):
#     for j in range(len(matrix1[0])):
#         resultmatrix[i][j]=matrix1[i][j]+matrix2[i][j]

# print(resultmatrix)   


# 4
# list=[2,23,45,6,4,33,4,55,4,3,34,4,45,4,34,43,4,5443,34,55,43,34,534534,5345,34534,5345,23,2342,342,5]
# m=int(input("please input m : "))
# if m>len(list):
#     print("ERROR!")
# else:
#     for i in range(-1,-(m+1),-1):
#         element=list.pop(-1)
#         list.insert(0,element)
#     print(list)

#5
# 可变数据类型： 
# - 列表（list） 
# - 字典（dict） 
# - 集合（set） 
 
# 不可变数据类型： 
# - 数字类型（int，float，complex） 
# - 字符串（str） 
# - 元组（tuple） 
# - 布尔类型（bool） 

#6
#第六题图片看不了啊，是空白的🥹