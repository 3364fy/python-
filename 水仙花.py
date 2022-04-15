for a in range(100,1000):
   ge=a%10
   shi=a//10%10
   bai=a//100
   if bai**3+shi**3+ge**3==a:
       print(a)

