class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        dp = [0] * (len(text2) + 1)

        for i in reversed(range(len(text1))):
            prev = 0
            for j in reversed(range(len(text2))):
                temp = dp[j]
                if text1[i] == text2[j]:
                    print(temp)
                    print(prev)
                    dp[j] = 1 + prev
                else:
                    dp[j] = max(dp[j], dp[j + 1])
                prev = temp
            print(dp)
        return dp[0]