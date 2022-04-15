class Car:
    def __init__(self,brand):
        self.brand=brand
    def start(self):
        print('汽车已启动...')
car=Car('宝马X5')
car.start()
print(car.brand)
print('--------------------------------------------------------------------------------------')
class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age#age不希望在类的外部使用，所以加了两个__
    def show(self):
        print( self.name,self.__age)
stu1=Student('张三',20)
stu1.show()
#在类的外部使用name和age
print(stu1.name)
#print(stu1.__age)
print(dir(stu1))
print(stu1._Student__age)#可以通过_Student__age访问，全靠自觉性