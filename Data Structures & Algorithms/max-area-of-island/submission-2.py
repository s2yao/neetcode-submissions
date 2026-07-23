class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ret = 0
        visited = set()
        height = len(grid) - 1
        width = len(grid[0]) - 1
        
        # checking current posn validity
        def check(row, col):
            if grid[row][col] == 1 and (row, col) not in visited:
                return True
            return False

        # prob all consec land and keep count
        # dynamcially update visit set
        def dfs(process) -> int:
            island_max = 1

            while process:
                row, col = process.pop()

                directions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]

                for direction in directions:
                    probe_row, probe_col = direction
                    # check in bound or not
                    if probe_row < 0 or probe_col < 0 or probe_row > height or probe_col > width:
                        continue
                    if check(probe_row, probe_col):
                        island_max += 1
                        process.append((probe_row, probe_col))
                        visited.add((probe_row, probe_col))
            
            return island_max

        # 2 for loop
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if check(row, col):
                    # add only 1 posn in visited
                    visited.add((row, col))
                    ret = max(dfs([(row, col)]), ret)

        return ret