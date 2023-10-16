# 1
# python的魔术方法就是在类中定义的方法，魔术方法不需要调用，而是会在执行特定功能时自动调用的方法
# 通过实现这些魔术方法来改变对象的默认行为，从而实现更加灵活和自定义化的类

import math

class Point:
    def __init__(self,x,y,z=0) -> None:
        self.x=x
        self.y=y
        self.z=z
        print(f"创建了Point({self.x},{self.y},{self.z})")
        #要求Point类在类初始化和销毁的时候分别输出 创建了Point(x, y, z) 和销毁了Point(x, y, z) 

    def __del__(self):
        print(f"销毁了Point({self.x},{self.y},{self.z})")
        #要求Point类在类初始化和销毁的时候分别输出 创建了Point(x, y, z) 和销毁了Point(x, y, z) 

    def __add__(self,other):#Point类加减Vector类得到新的Point类
        if isinstance(other,Vector):
            return Point(self.x+other.x,self.y+other.y,self.z+other.z)
        else:#Point类加 Point类报错
            raise TypeError("不支持两个Piont类型的加法")
        
    def __sub__(self,other):
        if isinstance(other,Vector):#Point类加减Vector类得到新的Point类
            return Point(self.x-other.x,self.y-other.y,self.z-other.z)
        elif isinstance(other,Point):#Point类减Point类得到新的Vector
            return Vector(self.x-other.x,self.y-other.y,self.z-other.z)
        else:
            raise TypeError("格式错误")
    
    def __eq__(self,other):
        if isinstance(other,Vector):
            return False
        elif isinstance(other,Point):#当且仅当x、y、z全部相等，Point和Vector类==才是true
            return self.x==other.x and self.y==other.y and self.z==other.z
        else:
            raise TypeError("格式错误")
        
    def __lt__(self,other):
        if isinstance(other,Point):#当对Point类来说，A点到原点的距离⼩于B到原点的距离时，A<B为true
            distance_self=math.sqrt(self.x**2+self.y**2+self.z**2)
            distance_other=math.sqrt(other.x**2+other.y**2+other.z**2)
            return distance_self<distance_other
        else:
            raise TypeError("格式错误")
        
    def __repr__(self):
        return f"Point({self.x},{self.y},{self.z})"
    

class Vector:
    def __init__(self,x,y,z=0):
        self.x=x
        self.y=y
        self.z=z
    
    def __add__(self,other):
        if isinstance(other,Vector):#实现向量的加法和减法
            return Vector(self.x+other.x,self.y+other.y,self.z+other.z)
        elif isinstance(other,Point):#Point类加减Vector类得到新的Point类
            return Point(self.x+other.x,self.y+other.y,self.z+other.z)
        else:
            raise TypeError("格式错误")
        
    def __sub__(self,other):
        if isinstance(other,Vector):
            return Vector(self.x-other.x,self.y-other.y,self.z-other.z)
        elif isinstance(other,Point):
            return Point(self.x-other.x,self.y-other.y,self.z-other.z)
        else:
            raise TypeError("格式错误")
        
    def __mul__(self,angle):# *x表⽰逆时针旋转x度
        radian=math.radians(angle)
        x_new = self.x * math.cos(radian) - self.y * math.sin(radian)
        y_new = self.x * math.sin(radian) + self.y * math.cos(radian)
        return Vector(x_new, y_new, self.z)
    
    def __truediv__(self, angle):# /x表⽰顺时针旋转x度
        radian = math.radians(angle)
        x_new = self.x * math.cos(radian) + self.y * math.sin(radian)
        y_new = -self.x * math.sin(radian) + self.y * math.cos(radian)
        return Vector(x_new, y_new, self.z)
    
    def __repr__(self):
        return f"Vector({self.x},{self.y},{self.z})"
    


p1=Point(1,2,3)
v1=Vector(1,4,7)
# p3=p1 + v1
# print(p3)

v2=Vector(8,28,29)
# print(v1+v2)

v3=Vector(2,3,1)
print(v2==v3)

    
        

