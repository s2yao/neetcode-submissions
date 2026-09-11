class Solution:
    def countSubstrings(self, s: str) -> int:
        # dp[left][right] = Is s[left:right+1] palin.
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        ret = 0

        for right in range(len(s)):
            for left in range(right + 1):
                window_size = right - left + 1
                if s[left] == s[right] and (window_size <= 3 or dp[left + 1][right - 1]):
                    dp[left][right] = True
                    ret += 1
        
        return ret 