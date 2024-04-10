arr=[12,4,-22,543,3443,5]
small=arr[0]
large=arr[0]
for i in arr:
    if i>large:
        large=i
    if i<small:
        small=i
print(small,large)