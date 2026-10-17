from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        # explore all possible choices available
        def dfs_backtrack(idx1, idx2):
            if idx2 == len(word2):
                return len(word1) - idx1
            if idx1 == len(word1):
                return len(word2) - idx2

            char1 = word1[idx1]
            char2 = word2[idx2]
            # normal
            if char1 == char2:
                return dfs_backtrack(idx1 + 1, idx2 + 1)

            curr_min_op = float("inf")
            # insert
            curr_min_op = min(curr_min_op, dfs_backtrack(idx1, idx2 + 1))
            # delete
            curr_min_op = min(curr_min_op, dfs_backtrack(idx1 + 1, idx2))
            # replace
            curr_min_op = min(curr_min_op, dfs_backtrack(idx1 + 1, idx2 + 1))
            
            return curr_min_op + 1
        
        return dfs_backtrack(0, 0)

# intention
# execution
