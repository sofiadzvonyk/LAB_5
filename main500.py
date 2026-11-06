a=input().split(',')
b=[]
for x in a:
    c=[]
    for y in x.split():
        c.append(int(y))
    b.append(c)
print(b)
b.sort(key=lambda x: x[1])
print(b)