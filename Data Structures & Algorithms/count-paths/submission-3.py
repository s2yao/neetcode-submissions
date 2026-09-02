class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * (n - 1)
        if not dp:
            return 1
        for _ in range(m - 1):
            for col in range(n - 1):
                if col == 0:
                    dp[col] += 1
                else:
                    dp[col] += dp[col - 1]
        
        return dp[-1]

        


        
        # dp = [[0] * n] * m

        # for row in range(m):
        #     for col in range(n):
        #         if row == 0 or col == 0:
        #             dp[row][col] = 1
        #         else:
        #             left = dp[row][col - 1]
        #             up = dp[row - 1][col]
        #             dp[row][col] = left + up
        
        # return dp[-1][-1]