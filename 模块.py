#包含函数、类、语句
#类包含类属性，实例方法，实例属性，类方法，静态方法，
#n个模块组成包，n个包组成Python程序，有利于团队协作开发
import math#数学模块
#使用import只能调用包名与模块名
print(dir(math))
print(math.pi)
print(math.pow(2,3))#float类型
print(math.ceil(9.1))
print(math.floor(99.99999))
print('---------------------------------------------------')
from math import pi#可以导入模块名，包名，函数名。变量名
print(pi)
print(pow(2,3))#int类型