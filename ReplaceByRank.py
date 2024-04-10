arr1=[100,2,70,12,90] #2,12,70,90,100
arr2=sorted(arr1)
for i in range(len(arr1)):
    temp=arr1[i]
    arr1[i]=(arr2.index(temp))+1
print(arr1)
