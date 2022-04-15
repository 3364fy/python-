item=['a','b','c']
prices=[100,25,322]
d={item:prices for item,prices in zip(item,prices)}
print(d)
