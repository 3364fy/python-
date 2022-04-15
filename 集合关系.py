a={1,2,3,4}
b={4,2,1,3}
print(a==b)
c={1,2,3,4,5,6,7,8}
print(a.issubset(c))#包含于
print(c.issuperset(a))#包含
print(a.isdisjoint(c))#无交集