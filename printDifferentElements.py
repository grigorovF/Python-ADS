def findDistinct(arr):
    n = len(arr)
    arr.sort()
    elem = None
    distinct = []
    for i in range(0, n):
        if (arr[i]!=elem):
            distinct.append(arr[i])
        elem = arr[i]

    return distinct

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    res = findDistinct(arr)
    for ele in res:
        print(ele, end=" ")