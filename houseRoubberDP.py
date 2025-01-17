def houseRobber(nums):
    n = len(nums)
    if n==0:
        return 0
    if n==1:
        return nums[0]
    
    prev1, prev2 = 0, 0
    for num in nums:
        current = max(prev1, prev2+num)
        prev2 = prev1
        prev1 = current
    
    return prev1

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    result = houseRobber(nums)
    print("max = ", result)