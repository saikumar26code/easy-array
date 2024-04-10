arr=[3,4,57,45,3,53,45,43,3]
n=len(arr)
arr.sort()
for i in range(n//2):
    print(arr[i],end="")
for j in range(n-1,n//2-1,-1):
    print(arr[j],end="")
print(arr)