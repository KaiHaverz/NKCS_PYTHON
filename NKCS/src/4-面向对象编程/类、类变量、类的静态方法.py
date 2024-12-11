class Student:
    student_num=0; #类变量

    def __init__(self,name,sex):
        self.name=name
        self.sex=sex
        Student.student_num+=1 #通过类名来访问类变量，增加一个学生，数量就加一

    #类方法
    #也需要通过类名来调用
    @classmethod
    def add_students(cls,add_num):
        cls.student_num+=add_num

    @classmethod
    def from_string(cls,info):
        name,sex=info.split(" ")
        return cls(name,sex)

    # 静态方法，没有参数，不能访问类和实例里面的私有属性
    @staticmethod # 获取名字长度
    def name_len(name):
        return len(name)

#类变量
s1=Student("Ganchao","male")
print(f"Student.student_num={Student.student_num}")
print(s1.student_num)  #通过实例来访问也不会报错，统一通过类名访问比较好

#类方法
my_friends=("Pengjia male")
s2=Student.from_string(my_friends)
print(f"Student.student_num={Student.student_num}")

# 使用类方法替代构造方法
import datetime

# 静态方法
print(f"s2.name:{s2.name},len of s2.name:{Student.name_len(s2.name)}") # 调用静态方法时，要通过类名来调用


# 总结
# 类变量定义在类里面，通过类名访问
# 类方法使用装饰器 classmethod(cls,)第一个变量就是类本身cls
# 静态方法使用装饰器 staticmethod 没有参数，不可以访问类的内部信息
