class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[-1] = 1

        for i in reversed(range(len(s))):
            if s[i] == '0':
                continue
            
            dp[i] += dp[i+1]
            if i + 1 >= len(s):
                continue
            curr_2_digit = s[i:i+2]
            if '10' <= curr_2_digit <= "26":
                dp[i] += dp[i+2]
                
        return dp[0]