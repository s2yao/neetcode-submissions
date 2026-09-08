class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        def check(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return False
            if (row, col) in visited:
                return False
            if grid[row][col] != 1:
                return False
            return True

        def bfs(row, col):
            if not check(row, col):
                return 0
            visited.add((row, col))
            res = 0
            directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            for d in directions:
                res += bfs(row + d[0], col + d[1])
            
            return res + 1

        ret = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if check(row, col):
                    ret = max(ret, bfs(row, col))
        
        return ret