class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]

        # dp[i][j] to record number of palindrome between index i and j
        ret = 0
        for right in range(len(s)):
            for left in range(right + 1):
                if s[left] == s[right] and (right - left <= 2 or dp[left + 1][right - 1]):
                    dp[left][right] = True
                    ret += 1
        
        return ret