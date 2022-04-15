def fy():
    global age#局部变量变全局变量
    age=20
    print(age)
fy()
print(age)