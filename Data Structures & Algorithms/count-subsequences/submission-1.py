from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0

        @cache
        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0 

            curr_comb = 0
            if i < len(s) and s[i] == t[j]:
                curr_comb += dfs(i + 1, j + 1)
            curr_comb += dfs(i + 1, j)
            return curr_comb
        dfs(0, 0)
        return dfs(0, 0)


# s = "cccataaaaaat", t = "cat"


# c : 3
# a : 1
# t : 1

# curr = 3

# stack = [c : 3 a : 6 t : 1]