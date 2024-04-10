arr=[4,-5,2,6,-8,3,2]
mid=len(arr)//2
firsthalf=arr[:mid]
secondhalf=arr[mid:len(arr)]
firsthalf.sort()
secondhalf.sort(reverse=True)
print(firsthalf+secondhalf)


