arr=[2,4,5,3,5,6,2,3]
ans=-1
for i in range(1,len(arr)):
    if sum(arr[:i])==sum(arr[i+1:]):
        ans=i
        break
print(ans) #not solved