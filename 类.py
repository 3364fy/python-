'''class Student:#由一个或多个单词组成，首字母大写
print(id(Student))
print(type(Student))
print(Student)'''
class Student:
    native_pace='河北'#类属性
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def fy(self):#实例方法
        print('学生在吃饭')
#静态方法
    @staticmethod
    def methon():
        print('静态方法')
#类方法
    @classmethod
    def cm(cls):
        print('类方法')
#创建Student类的对象
stu1=Student('张三',20)
'''print(id(stu1))
print(type(stu1))
print(stu1)
print('---------------------------------------')
print(id(Student))#Student是类的名称
print(type(Student))
print(Student)'''
stu1.fy()
#类属性的使用方式
print(stu1.name)
print(stu1.age)
Student.fy(stu1)
print(Student.native_pace)
stu3=Student('王五',20)
stu4=Student('冯六',40)
print(stu3.native_pace)
print(stu4.native_pace)
Student.native_pace='北京'
print(stu3.native_pace)
print(stu4.native_pace)
print('--------------类方法的使用方式-------------')
Student.cm()
print('------------静态方法的使用方式-----------------')
Student.methon()