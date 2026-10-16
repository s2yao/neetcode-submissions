
from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        def check_bound(row, col):
            if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
                return False
            return True
        
        directions =  [[-1, 0], [0, -1], [1, 0], [0, 1]]
        @cache
        def backtrack(row, col):
            curr_max_path = 1

            for dr, dc in directions:
                probe_row, probe_col = row + dr, col + dc
                if not check_bound(probe_row, probe_col):
                    continue
                if matrix[row][col] >= matrix[probe_row][probe_col]:
                    continue
                curr_max_path = max(curr_max_path, backtrack(probe_row, probe_col) + 1)
            
            return curr_max_path
        
        ret_max = 1
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                ret_max = max(ret_max, backtrack(row, col))
        
        return ret_max