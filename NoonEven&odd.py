arr=[int(x) for x in input().split()]
ce,co=0,0
for i in arr:
    if i%2==0:
        ce+=1
    else:
        co+=1
print(ce,co)