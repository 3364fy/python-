a=input('您是会员吗')
if a=='是':
    money=int(float(input('输入您的金额')))
    if money>=200:
        money*=0.8
    else:money*=0.9
else: money=input('输入您的金额')
print(money)