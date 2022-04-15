a=[1,65,6,56,5,65,326,656,6565]
a.remove(65)
print(a)
a.pop(1)
print(a)
a.pop()
print(a)
b=a[1:4]
print(b)
a[1:4]=[]
print(a)
c=a
c.clear()
print(c)
del b
print(b)

