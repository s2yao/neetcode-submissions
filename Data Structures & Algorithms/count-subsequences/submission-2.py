class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]

        for col in range(len(s) + 1):
            dp[len(t)][col] = 1
        
        # for row in dp:
            # print(row)
        
        for row in reversed(range(len(t))):
            for col in reversed(range(len(s))):
                curr_char = s[col]
                target_char = t[row]

                # suffix prev elements can reach
                dp[row][col] = dp[row][col+1]
                # suffix curr element can reach
                if curr_char == target_char:
                    dp[row][col] += dp[row+1][col+1]

        
        return dp[0][0]