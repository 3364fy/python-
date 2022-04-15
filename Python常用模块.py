import sys
print(sys.getsizeof(28))#占用内存
import time
print(time.time())
print(time.localtime(time.time()))
import urllib.request
print(urllib.request.urlopen('http://www.baidu.com').read())
