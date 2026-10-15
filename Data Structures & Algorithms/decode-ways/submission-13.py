class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[-1] = 1

        for i in reversed(range(len(s))):
            curr_digit = s[i]
            if curr_digit == '0':
                continue
            
            # single digit
            dp[i] += dp[i + 1]
            # 2 digits
            if i + 2 <= len(s):
                if "10" <= s[i:i+2] <= "26":
                    dp[i] += dp[i + 2]

        return dp[0]