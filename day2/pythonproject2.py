#1

# input_str=input()
# count1=0
# count2=0
# count3=0
# count4=0
# for char in input_str:
#     if char.isalpha():
#         count1+=1
#     elif char.isspace():
#         count2+=1
#     elif char.isdigit():
#         count3+=1
#     else:
#         count4+=1
# print(count1,count2,count3,count4)


# 2
# a = input()
# n = int(input("请输入一个正整数 n: "))
# s = 0
# current_term = 0

# for i in range(n):
#     current_term = current_term * 10 + int(a)
#     s += current_term
# print(s)



# 3

# initial_height = 100
# num_bounces = 10
# total_distance = 0
# current_height = initial_height
# for _ in range(num_bounces):
#     total_distance += current_height
#     current_height /= 2

# print("第10次落地时，共经过的距离：", total_distance, "米")
# print("第10次反弹的高度：", current_height, "米")

# 4

# for num in range(100, 1000):
#     # 分解数字的百位、十位和个位
#     hundreds = num // 100
#     tens = (num % 100) // 10
#     ones = num % 10
#     cube_sum = (hundreds ** 3) + (tens ** 3) + (ones ** 3)
#     if cube_sum == num:
#         print(num)

# 5

# def is_prime(num):
#     if num <= 1:
#         return False
#     if num == 2:
#         return True
#     if num % 2 == 0:
#         return False
#     for i in range(3, int(num ** 0.5) + 1, 2):
#         if num % i == 0:
#             return False
#     return True

# for number in range(101, 201):
#     if is_prime(number):
#         print(number)