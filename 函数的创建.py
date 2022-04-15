def fy(a,b):
    c=a+b
    return c
result=fy(33,64)
print(result)

def fun(arg1,arg2):
    print('arg1',arg1)
    print('arg2',arg2)
    arg1=100
    arg2.append(10)
    print('arg1', arg1)
    print('arg2', arg2)
    return
n1=88
n2=[11,55,66]
fun(n1,n2)

def fun(num):
    odd=[]
    even=[]
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even
a=fun((1,5,2,51,323,4,13,65))
print(a)

def fun(a,b=10):
    print(a,b)
fun(100)
fun(10,80)

def fy(*agrs):
    print(agrs)
fy(10)
fy(10,80)
fy(10,80,90)

def fy1(**agrs):
    print(agrs)
fy1(a=10)
