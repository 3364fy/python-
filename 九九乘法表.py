for a in range(1,10):
    for b in range(1,a+1):
        c=a*b
        print(str(a)+'*'+str(b)+'='+str(c),end='\t')
    print()
for i in range(5):
    for j in range(1,11):
        if j%2==0:
            #break
            continue
        print(j,end='\t')
    print()