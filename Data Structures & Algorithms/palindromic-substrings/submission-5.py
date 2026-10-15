class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        ret = 0
        for left in reversed(range(len(s))):
            for right in range(left, len(s)):
                if s[left] != s[right]:
                    continue
                
                curr_window = right - left + 1
                if curr_window <= 2:
                    dp[left][right] = True
                else:
                    dp[left][right] = dp[left + 1][right - 1]
                
                if dp[left][right]:
                    ret += 1
        
        return ret