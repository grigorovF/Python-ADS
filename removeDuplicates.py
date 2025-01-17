#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
class Solution:
    def removeDuplicates(self, arr):
        n = len(arr)
        arr.sort()
        elem = None
        distinct = []
        for i in range(0, n):
            if (arr[i]!=elem):
                distinct.append(arr[i])
            elem = arr[i]
        
        return distinct

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.removeDuplicates(arr)
        print(*ans)
        print("~")
        t -= 1

