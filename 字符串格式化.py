name='张三'
age=20
print('我叫%s,今年%d岁' % (name,age))
print('我叫{0},今年{1}岁'.format(name,age))
print(f'我叫{name},今年{age}岁')
print('%10d' % 99)#长度为10
print('%.3f' % 3.1415926)#保留三位小数
print('%10.3f' % 3.1415926)#长度为10，保留三位小数
print('{0:.3}'.format(3.1415926))#3位有效数字
print('{0:.3f}'.format(3.1415926))
print('{0:10.3f}'.format(3.1415926))
