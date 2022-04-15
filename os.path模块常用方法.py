import os.path
#目录相关操作
print(os.path.abspath('a.txt'))#文件路径
print(os.path.exists('a.txt'),os.path.exists('f.txt'))#判断文件是否存在
print(os.path.join('E\\python','a.txt'))#文件路径拼接
print(os.path.split('E\\python\\a.txt'))#分离文件名与扩展名
print(os.path.splitext('E\\python\\a.txt'))#分离后缀
print(os.path.basename('E\\python\\a.txt'))#提取文件名
print(os.path.dirname('E\\python\\a.txt'))#提取文件目录
print(os.path.isdir('E\\python\\a.txt'))#判断是否为目录
