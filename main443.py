a=[]
for x in input().split():
    a.append(int(x))
b=[]
b.append(a[-1])
del a[-1]
b.extend(a)
print(b)