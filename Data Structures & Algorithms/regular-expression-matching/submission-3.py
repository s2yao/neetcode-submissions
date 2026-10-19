from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def can_match(i, j):
            if i >= len(s):
                return False
            if p[j] == ".":
                return True
            return s[i] == p[j]

        @cache
        def dfs(i, j):
            if j == len(p):
                return i == len(s)

            # Case 1: Pattern contains *
            if j + 1 < len(p) and p[j + 1] == "*":

                # Option A: Match zero occurrences
                if dfs(i, j + 2):
                    return True

                # Option B: Match one or more occurrences
                if can_match(i, j):
                    return dfs(i + 1, j)

                return False

            # Case 2: Normal character matching
            if not can_match(i, j):
                return False

            return dfs(i + 1, j + 1)
        return dfs(0, 0)