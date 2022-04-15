print(dir(object))
class A(object):
    pass
class B(object):
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age
#创建C类的对象
x=C('jack',20)#x是C类型的一个实例对象
print(x.__dict__)#实例对象的属性字典
print(C.__dict__)
print('-------------------------------')
print(x.__class__)#<class '__main__.C'>输出了对象所属的类
print(C.__bases__)#C类的父类类型的元素
print(C.__base__)#输出最近的父类（类的基类）
print(C.__mro__)#类的层次结构
print(A.__subclasses__())#A的子类的列表


