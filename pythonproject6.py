# 1


# python 的type函数的返回值为参数的类型，
# 因为a,b都为元祖，因此返回“元祖”类型，而第二行输出即为元祖a，第三行的输出为一个逻辑值，
# 因为代码第5行的print的是逻辑表达式，返回真。

# 首先声明了一个字典，存放键值对。让键1的值为2，让键（1，2）元祖的值为1，然后打印输出即可。


# a是一个二维列表，因此a[1][2]即是索引第一个列表的第二个元素，即就是3
# 而a[1,2]则自动被python封装称为元祖，无法作为列表的索引



# 2

# 输出：*运算执行了对元祖a的拆包，将a变成了独立的4个变量输出

# 利用3个变量x，y，z对元祖进行了拆分

# a=(1,2,3)
# x,y,_=a
# x,_,__=a
# x,_,_=a
# _,__,___=a
# print(x,_,__,___)
# x,*y=a
# x,*_=a
# print(*y,*_)

# 下划线或者双下划线或三下划线在python中也可以算作独立的变量，因此也可以用来进行元祖的拆分
# 而利用*y或者*_变量代表元祖其后的整体，所以会输出2，3


# 元祖的自动打包使得a，b整体成为了一个元祖变量
# a，b=b，a表示直接把b，a元祖赋值给a，b
# 因此实现了不引入第三个变量的交换


# 3
class Person:
    name=None
    age=None
    gender=None
    
    def personInfo(self):
        print(f"name is {self.name},age is {self.age},gender is {self.gender}")

class Student(Person):
    college=None
    stuclass=None

    def personInfo(self):
        super().personInfo()
        print(f"college is {self.college},class is {self.stuclass}")
    def __str__(self):
        return f"name is {self.name},age is {self.age},gender is {self.gender},college is {self.college},class is {self.stuclass}"
    

stu=Student()
stu.name='will'
stu.age=20
stu.gender="male"
stu.college="electricity and information"
stu.stuclass="2203"
print(stu)    
stu.personInfo()

