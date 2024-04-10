arr=[8,5,9,3,3,25,4,62,3]
small = float('inf')  # Initialize 'small' to positive infinity
second = float('inf')  # Initialize 'second' to positive infinity
for i in arr:
    if i < small:
        second = small
        small = i
    elif i < second and i != small:  # Update 'second' only if the element is smaller than the current 'second' and not equal to 'small'
        second = i
print(second) 
