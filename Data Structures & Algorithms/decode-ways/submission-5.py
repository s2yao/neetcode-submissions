class Solution:
    def numDecodings(self, s: str) -> int:
        dp1 = 1  # dp[idx + 1]
        dp2 = 0  # dp[idx + 2], irrelevant on first iteration

        for idx in range(len(s) - 1, -1, -1):
            curr_result = 0

            if s[idx] != "0":
                curr_result += dp1

                if idx + 1 < len(s) and 10 <= int(s[idx:idx + 2]) <= 26:
                    curr_result += dp2

            dp2, dp1 = dp1, curr_result

        return dp1