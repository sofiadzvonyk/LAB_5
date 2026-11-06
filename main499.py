a=[]
for x in input():
    a.append(int(x))
mini=sorted(a)
maxi=mini.copy()
maxi.reverse()
if mini[0]==0:
    for i in range(1, 4):
        if mini[i]!=0:
            mini[0], mini[i]=mini[i], mini[0]
            break
print(''.join(map(str, mini)) + " " + ''.join(map(str, maxi)))