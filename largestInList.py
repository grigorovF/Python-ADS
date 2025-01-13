def findMax(arr):
    if not arr:
        return None
    else:
        return max(arr)


arr = list(map (int, input().split()))
result = findMax(arr)
print("The largest element is ", result)