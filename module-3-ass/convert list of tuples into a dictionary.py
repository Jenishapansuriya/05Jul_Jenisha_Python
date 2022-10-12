l = [("Name", "Ram"), ("Name", "Pooja"), ("Name", "Sara"), ("Age", 21), ("Gender", "Male"), ("Age", 23), ("Gender", "Female"), ("Gender", "Female") , ("Age", 22)]
dic = {}
for x, y in l:
    dic.setdefault(x, []).append(y)
print (dic)