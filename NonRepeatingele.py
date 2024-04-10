arr=[4,3,53,3,23,5,3,2,2]
d={}
for i in arr:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
nonrepeat=[k for k,v in d.items() if v==1]
print(nonrepeat)