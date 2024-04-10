arr=[2,5,3,6,3,5,3,5,2]
d={}
for i in arr:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
res=d.items()
print(res)