class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m <= 1 or n <= 1:
            return 1
        dp = [[0] * (n - 1) for _ in range((m - 1))] 

        for row in range(m - 1):
            for col in range(n - 1):
                if row == 0 and col == 0:
                    dp[row][col] = 2
                elif row == 0:
                    dp[row][col] = dp[row][col - 1] + 1
                elif col == 0:
                    dp[row][col] = dp[row - 1][col] + 1
                else:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        
        return dp[-1][-1]
