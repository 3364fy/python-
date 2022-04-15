s='萦损柔肠'
print(s.encode(encoding='GBK'))#在GBK这种编码格式中，一个中文占两个字节
print(s.encode(encoding='UTF-8'))#在GBK这种编码格式中，一个中文三个字节

#解码
byte=s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))
byte=s.encode(encoding='UTF-8')
print(byte.decode(encoding='UTF-8'))