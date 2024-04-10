def numequal(arr):
    for i in range(len(arr)):
        while arr[i]%2==0:
            arr[i]//=2
        while arr[i]%3==0:
            arr[i]//=3
    if arr[i]!=arr[0]:
        return False
    return True
arr=[50,100,130]
if numequal(arr):
    print("yes")
else:
    print("no")