def fy(n):
    if n==1:
        return 1
    else:return n*fy(n-1)
print(fy(6))

def fy1(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:return fy1(n-1)+fy1(n-2)
print(fy1(6))
for n in range(1,10):
   print(fy1(n))
