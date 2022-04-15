a=20
b=90
c=a+b#两个整数类型的相加操作，调用以下函数
d=a.__add__(b)
print(c)
print(d)

class Student():
    def __init__(self,name):
        self.name=name
    def __add__(self, other):
        return self.name+other.name
    def __len__(self):
        return len(self.name)
stu1=Student('张三')
stu2=Student('李四')
s=stu1+stu2
print(s)#实现了两个对象的加法运算（因为在Student类中编写了__add__()特殊方法）
s=stu1.__add__(stu2)
print(s)
print('-----------------------------------------------')
lst=[11,22,33,44,55]
print(len(lst))#内置函数len,查看列表长度
print(lst.__len__())
print(len(stu1))#不写len方法会报错：类型错误：“学生”类型的对象没有 len()
