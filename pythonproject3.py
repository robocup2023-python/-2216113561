# 1

# def find_total_peaches():
#     peaches = 1
#     for day in range(9, 0, -1):
#         peaches = (peaches + 1) * 2
#     return peaches

# total_peaches = find_total_peaches()
# print("第1天共摘了 {} 个桃子".format(total_peaches))







# 2


# str='*'
# for i in range(1,5):
#     print((4-i)*' ',end='')
#     print(str.center(2*i-1,'*'))
# for j in range(3,0,-1):
#     print((4-j)*' ',end='')
#     print(str.center(j*2-1,'*'))



# 3
# use str() to tranfer a number into string
# number=12321
# weishu=0
# s=str(number)
# for i in s:
#     weishu+=1

# i=0
# j=weishu-1
# while i<j:
#     if s[i]==s[j]:
#         i+=1
#         j-=1
#     else:
#         print("is not huiwenshu")
#         break

# print("is huiwenshu")
    
    


# 4


# year=input("please input a year: ")
# if int(year)%4==0 and int(year)%100!=0:
#     print("is runnian")
# else:
#     print("is not runnian")
# if int(year)%100==0:
#     if int(year)%400==0:
#         print("is runnian")
#     else:
#         print("si not runnian")



#5

from datetime import datetime
year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入日期："))
date = datetime(year, month, day)


day_of_year = date.timetuple().tm_yday