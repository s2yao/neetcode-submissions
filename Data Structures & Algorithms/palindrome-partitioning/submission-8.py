class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []
        curr = []
        n = len(s)
        
        dp = [[False] * n for _ in range(n)]

        for left in reversed(range(n)):
            for right in range(left, n):

                if s[left] != s[right]:
                    continue

                # Single character or two matching characters
                if right - left <= 1:
                    dp[left][right] = True
                else:
                    dp[left][right] = dp[left + 1][right - 1]

        def backtrack(idx):
            if idx == len(s):
                ret.append(curr.copy())
                return
            
            for i in range(idx, len(s)):
                if not dp[idx][i]:
                    continue
                
                curr.append(s[idx:i+1])
                backtrack(i + 1)
                curr.pop()
        
        backtrack(0)
        return ret