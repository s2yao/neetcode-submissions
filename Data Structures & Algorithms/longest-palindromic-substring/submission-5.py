class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        ret = ""
        curr_max = 0

        for right in range(len(s)):
            for left in range(right + 1):
                if s[left] == s[right] and (right - left <= 2 or (dp[left + 1][right - 1])):
                    dp[left][right] = True
                    if right - left + 1 > curr_max:
                        curr_max = right - left + 1
                        ret = s[left:right+1]
        
        return ret