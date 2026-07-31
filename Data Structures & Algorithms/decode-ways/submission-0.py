class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[-1] = 1

        for idx in reversed(range(len(s))):
            if not int(s[idx]):
                continue
            # 1 char
            end_idx_1 = idx + 1
            dp[idx] += dp[end_idx_1]
            # 2 char
            if idx + 2 <= len(s):
                end_idx_2 = idx + 2
                if not 1 <= int(s[idx:end_idx_2]) <= 26:
                    continue
                dp[idx] += dp[end_idx_2]

        return dp[0]
            
