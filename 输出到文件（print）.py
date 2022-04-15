fp=open('D:/123.txt','a+')
print('helloworld',file=fp)

print('hello','world',file=fp)
print('helloworld','fy',file=fp)
print('helloworld','fy',file=fp)
fp.close()