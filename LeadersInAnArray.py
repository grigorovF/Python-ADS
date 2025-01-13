def leaders(arr):
    n = len(arr)
    
    arrLeaders = []
    leader = arr[-1]
    arrLeaders.append(leader)
    

    for i in range(n-2, -1, -1):
        if (arr[i]>leader):
            arrLeaders.append(arr[i])
            leader = arr[i]
    return arrLeaders[::-1]

arr = list(map(int, input().split()))
result = leaders(arr)
print(" ".join(map(str, result)))