class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
            
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        dp[0][0] = True

        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if not dp[i][j]:
                    continue
                
                if i < len(s1) and s1[i] == s3[i+j]:
                    dp[i + 1][j] = dp[i][j]
                if j < len(s2) and s2[j] == s3[i+j]:
                    dp[i][j + 1] = dp[i][j]
        
        return dp[-1][-1]