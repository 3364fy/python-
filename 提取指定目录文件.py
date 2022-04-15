import os
path=os.getcwd()
lst=os.listdir(path)
for filename in lst:
    print(path)
    print(lst)
    if filename.endswith('.py'):
        print(filename)
