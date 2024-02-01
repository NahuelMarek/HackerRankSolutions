
n = 5
arr = [2,3,6,6,5]

arr.sort()
print(arr)
max=arr[-1]
for i in range(n-1,-1,-1):
    if max>arr[i]:
        max=arr[i]
        break
print(max)


