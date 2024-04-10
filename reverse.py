arr=[2,4,6,844,4]
start=0
end=len(arr)-1
for i in range(len(arr)//2):
    if start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
print(arr)
