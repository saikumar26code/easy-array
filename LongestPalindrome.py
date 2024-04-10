
def ispali(arr):
    if arr[::-1]==arr:
        return arr
    
g=["abca","aba","dhu"]
maxlen=0
for arr in g:
    if ispali(arr):
        if len(arr)>maxlen:
            maxlen=len(arr)
            longest=arr
print(longest)

