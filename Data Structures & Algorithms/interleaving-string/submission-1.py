from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def backtrack(i, j):
            # Successfully consumed both strings
            if i == len(s1) and j == len(s2):
                return True

            k = i + j

            # Choice 1: Take from s1
            if i < len(s1) and s1[i] == s3[k]:
                if backtrack(i + 1, j):
                    return True

            # Choice 2: Take from s2
            if j < len(s2) and s2[j] == s3[k]:
                if backtrack(i, j + 1):
                    return True

            return False

        return backtrack(0, 0)