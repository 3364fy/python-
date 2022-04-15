file=open('a.txt','r',encoding='utf-8')
print(file.readlines())
file.close()
file=open('b.txt','w')#没有则创建，有则覆盖
file.write('hello,world')
file.close()
file=open('b.txt','a')#没有则创建，有则在末尾追加
file.write('\npython')
file.close()
#图片拷贝
src_file=open('女生 女子 起床 晚上 都市 夜景 4k动漫壁纸_彼岸图网.jpg','rb')
target_file=open('copy女生 女子 起床 晚上 都市 夜景 4k动漫壁纸_彼岸图网.jpg','wb')
target_file.write(src_file.read())
target_file.close()
src_file.close()
#指针位置变换
a=open('a.txt','r',encoding='utf-8')#utf-8一个中文三个字节
a.seek(3)
print(a.tell())
print(a.read())
print(a.tell())
a.close()