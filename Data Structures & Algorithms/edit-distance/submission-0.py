class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [0] * (len(word1) + 1)

        for j in range(len(word1) + 1):
            dp[j] = len(word1) - j

        for i in reversed(range(len(word2))):
            prev = dp[len(word1)]
            dp[len(word1)] = len(word2) - i

            for j in reversed(range(len(word1))):
                temp = dp[j]

                if word1[j] == word2[i]:
                    dp[j] = prev
                else:
                    dp[j] = 1 + min(dp[j], dp[j + 1], prev)

                prev = temp

        return dp[0]