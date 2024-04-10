arr=[3,53,36,2,3,5,2,2,634,3,5,5]
d={}
for i in arr:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
repeatingele=[ke for ke,value in d.items() if value>1]
print(repeatingele)