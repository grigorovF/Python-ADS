def secondLargest(arr):
    arr.sort()
    n = len(arr) 

    for i in range(n-2, -1, -1):
        if arr[i] != arr[n-1]:
            return arr[i]
    return -1

arr = list(map(int, input().split()))
result = secondLargest(arr)
print("Second largest number is: ", result)