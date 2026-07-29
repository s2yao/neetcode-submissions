class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * n 
        dp[0] = 1
        dp[1] = 2
        for idx in range(2, n):
            dp[idx] = dp[idx - 1] + dp[idx - 2]
        
        return dp[-1]