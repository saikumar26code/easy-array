arr=[10,3,53,35,3,5,33,3]
res=[]
for i in arr:
    if i not in res:
        res.append(i)
print(len(res))

#use set
#use dictionary --> return len of dict