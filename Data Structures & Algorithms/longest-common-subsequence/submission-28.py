class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 < text2:
            text1, text2 = text2, text1
        dp = [0] * (len(text1) + 1)

        for i in reversed(range(len(text2))):
            char_target = text2[i]
            prev = dp.copy()
            for j in reversed(range(len(text1))):
                char_curr = text1[j]
                if char_curr != char_target:
                    dp[j] = max(dp[j+1], dp[j])
                else:
                    dp[j] = prev[j+1] + 1
        return dp[0]
        
        