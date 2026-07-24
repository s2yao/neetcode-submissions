class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set() # (row, col)
        ret = 0
        height = len(grid) - 1
        width = len(grid[0]) - 1
        
        # whether the current row, col is valid 
        def check(row, col) -> bool: # O(1)
            if grid[row][col] == "1" and (row, col) not in visited:
                return True
            return False

        # look 4 dir, process contains posn to step on
        def dfs(process: List) -> None: # O(nm)
            if not process:
                return

            while process:
                curr_row, curr_col = process.pop()
                directions = [(curr_row + 1, curr_col), (curr_row, curr_col + 1), (curr_row, curr_col - 1), (curr_row - 1, curr_col)]
                for direction in directions:
                    probe_row, probe_col = direction
                    if probe_row < 0 or probe_row > height or probe_col < 0 or probe_col > width:
                        continue
                    if check(probe_row, probe_col):
                        visited.add((probe_row, probe_col))
                        process.append((probe_row, probe_col))
            
        # searcher to find any "1"s
        # O(nm)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if check(row, col): # land that i havent step yet
                    visited.add((row, col))
                    dfs([(row, col)])
                    ret += 1

        return ret

