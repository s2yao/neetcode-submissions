class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ret = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != 1:
                return 0

            grid[row][col] = 0
            
            up = dfs(row - 1, col)
            down = dfs(row, col - 1)
            left = dfs(row + 1, col)
            right = dfs(row, col + 1)
            
            return up + down + left + right + 1
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    ret = max(ret, dfs(row, col))  
        
        return ret