class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text1) + 1)

        for i in reversed(range(len(text2))):
            prev = 0
            for j in reversed(range(len(text1))):
                temp = dp[j]
                if text2[i] == text1[j]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j + 1])
                prev = temp
        return dp[0]