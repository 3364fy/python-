a=input('请输入取款金额')
s=int(a)
money=1000
if s<=1000:
    money=1000-s
    print('取款成功，剩余金额',money)