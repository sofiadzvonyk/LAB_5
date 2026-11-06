a=[]
for x in input().split():
    a.append(int(x))
s=sum(a)
n=len(a)
av=s/n
print(f"{av:.2f}")