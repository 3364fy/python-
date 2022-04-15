scores={'张三':100,'李四':98,'王五':45}
print(scores)
print(type(scores))
a=dict(name='jack',age=20)
print(a)
d={}
print(d)

print(scores['张三'])
print(scores.get('张三'))
print(scores.get('马六'))
print(scores.get('马七','不存在'))