scores={'张三':100,'李四':98,'王五':45}
print('张三' in scores)
del scores['张三']
print(scores)
scores.clear()
print(scores)
scores['陈柳']=65
print(scores)
scores['陈柳']=35
print(scores)