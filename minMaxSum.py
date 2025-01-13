def minMaxSum(arr):
    minimum = min(arr)
    maximum = max(arr)

    return minimum+maximum

arr = list(map(int, input().split()))
result = minMaxSum(arr)
print("Result = ", result)