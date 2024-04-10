arr1=[int(ele) for ele in input().split()]
arr2=[int(ele) for ele in input().split()]
res=0
arr1.sort()
arr2.sort(reverse=True)
for i,j in zip(arr1,arr2):
    res+=i*j
print(res)