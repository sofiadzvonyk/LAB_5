even=[]
odd=[]
for x in input().split():
    x=int(x)
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)
even.reverse()
even.extend(odd)
print(even)