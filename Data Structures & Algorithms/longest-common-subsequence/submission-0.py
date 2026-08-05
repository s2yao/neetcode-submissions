class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Use the shorter string for dp to save space
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        dp = [0] * (len(text2) + 1)

        for i in reversed(range(len(text1))):
            old_diagonal = 0

            for j in reversed(range(len(text2))):
                old_below = dp[j]

                if text1[i] == text2[j]:
                    dp[j] = 1 + old_diagonal
                else:
                    dp[j] = max(
                        old_below,  # Skip text1[i]
                        dp[j + 1]   # Skip text2[j]
                    )

                old_diagonal = old_below

        return dp[0]