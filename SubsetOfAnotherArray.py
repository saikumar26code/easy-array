def subset(arr1,arr2):
    if arr1.union(arr2)==arr1:
        return "yes"
    return"no"
arr1=set([1,2,3,4,5,6,7])
arr2=set([1,2,4])
print(subset(arr1,arr2)) #dont know
    