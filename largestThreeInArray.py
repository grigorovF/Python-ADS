def findLargest(arr):
    arr.sort()
    n = len(arr)
    first = arr[n-1]
    for i in range(n-2, -1, -1):
        if (arr[i] != arr[n-1]):
            second = arr[i]
            break
    
    for i in range(n-3, -1, -1):
        if (arr[i] != first and arr[i] != second):
            third = arr[i]
            break
        
    return first , second, third


arr = list(map(int, input().split()))
result = list((findLargest(arr)))
print ("Largest numbers are: ", result)
           