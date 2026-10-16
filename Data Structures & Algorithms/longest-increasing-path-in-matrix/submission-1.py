from functools import cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        @cache
        def backtrack(row, col, prev):
            if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
                return 0
            if matrix[row][col] <= prev:
                return 0
            
            curr_max_path = 0
            for dr, dc in directions:
                curr_max_path = max(curr_max_path, backtrack(row + dr, col + dc, matrix[row][col]))
            
            return curr_max_path + 1
        
        ret_max = 1
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                ret_max = max(ret_max, backtrack(row, col, float('-inf')))
        
        return ret_max