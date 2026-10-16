from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def backtrack(idx1, idx2):
            if idx1 == len(s1) and idx2 == len(s2):
                return True

            k = idx1 + idx2

            if idx1 < len(s1) and s1[idx1] == s3[k]:
                if backtrack(idx1 + 1, idx2):
                    return True
            

            if idx2 < len(s2) and s2[idx2] == s3[k]:
                if backtrack(idx1, idx2 + 1):
                    return True
            
            return False

        return backtrack(0, 0)