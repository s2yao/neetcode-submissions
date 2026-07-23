class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        height = len(grid) - 1
        width = len(grid[0]) - 1

        def check(row, col):
            # if row < 0 or col < 0 or row > height or col > width:
            #     return False
            if (row, col) not in visited and grid[row][col] == "1":
                return True
            return False
 
        def dfs(process):
            while process:
                row, col = process.pop()
                visited.add((row, col))
                directions = [(row - 1, col), (row + 1, col), (row, col + 1), (row, col - 1)]

                for direction in directions:
                    probe_row, probe_col = direction
                    if probe_row < 0 or probe_col < 0 or probe_row > height or probe_col > width:
                        continue
                    if check(probe_row, probe_col):
                        process.append((probe_row, probe_col))
                
        ret = 0
        # 2 for loop traversing all elements
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # if curr ele in visited: continue
                if (row, col) in visited: continue
                # if not in visited, curr elemenet is 1
                if grid[row][col] == "1":
                    # put to dfs
                    dfs([(row, col)])
                    ret += 1
                # if not in visited, curr elemenet is 0
                else:
                    visited.add((row, col))
        
        return ret