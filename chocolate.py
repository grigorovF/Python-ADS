def calculateWaysToReachSum(n):
    dp = [0] * (n + 1)  # Array of size n+1
    dp[0] = 1  # 1 way to make sum 0 (no coins)
    
    for i in range(1, n + 1):
        if i - 1 >= 0:
            dp[i] += dp[i - 1]  # Use coin 1
        if i - 2 >= 0:
            dp[i] += dp[i - 2]  # Use coin 2
    
    return dp[n]

# Example usage
n = 4
print(f"Number of ways to reach the sum {n}: {calculateWaysToReachSum(n)}")