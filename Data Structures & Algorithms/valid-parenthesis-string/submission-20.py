
from functools import cache

class Solution:
    def checkValidString(self, s: str) -> bool:
        @cache
        def dfs_backtrack(idx, balance):
            if balance < 0:
                return False

            if idx == len(s):
                return balance == 0

            if s[idx] == '(':
                return dfs_backtrack(idx + 1, balance + 1)

            elif s[idx] == ')':
                return dfs_backtrack(idx + 1, balance - 1)

            else:
                as_left = dfs_backtrack(idx + 1, balance + 1)
                as_right = dfs_backtrack(idx + 1, balance - 1)
                as_empty = dfs_backtrack(idx + 1, balance)

                return as_left or as_right or as_empty

        return dfs_backtrack(0, 0)
