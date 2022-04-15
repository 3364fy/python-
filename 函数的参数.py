def fy(a,b,c):
    print('a=',a)
    print('b=',b)
    print('c=',c)
list=[10,20,30]
fy(*list)
dic={'a':10,'b':20,'c':30}
fy(**dic)

def fy1(a,b,*,c,d):
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)
fy1(10,20,c=30,d=40)
