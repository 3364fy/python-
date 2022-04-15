with open('b.txt','r') as file:
    print(file.read())#不用手动_.close
with open('copy女生 女子 起床 晚上 都市 夜景 4k动漫壁纸_彼岸图网.jpg','rb') as src_file:
    with open('copycopy女生 女子 起床 晚上 都市 夜景 4k动漫壁纸_彼岸图网.jpg','wb') as c_file:
        c_file.write(src_file.read())