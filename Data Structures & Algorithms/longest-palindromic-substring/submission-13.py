class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for _ in range(len(s))]
        best_left_idx = 0
        best_right_idx = 0

        for left in reversed(range(len(s))):
            for right in range(left, len(s)):
                if s[left] != s[right]:
                    continue
                curr_window = right - left + 1
                if curr_window <= 2:
                    dp[left][right] = True
                else:
                    dp[left][right] = dp[left + 1][right - 1]
                best_window = best_right_idx - best_left_idx + 1
                if dp[left][right] and curr_window > best_window:
                    best_right_idx = right
                    best_left_idx = left
        
        return s[best_left_idx:best_right_idx+1]
