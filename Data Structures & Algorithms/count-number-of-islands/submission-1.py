class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        height = len(grid) - 1 # row
        width = len(grid[0]) - 1 # col

        # if prob not visited and is land, append to process
        def valid(row, col):
            if (row, col) not in visited and grid[row][col] == "1":
                return True

        # goes through all the adjacent land of initial posn
        def dfs(process):
            if not process:
                return
        
            # pop current posn
            row, col = process.pop()

            # add to set
            visited.add((row, col))

            # up
            if row != 0:
                if valid(row - 1, col):
                    process.append((row - 1, col))
            # down
            if row != height:
                if valid(row + 1, col):
                    process.append((row + 1, col))
            # left
            if col != 0:
                if valid(row, col - 1):
                    process.append((row, col - 1))
            # right
            if col != width:
                if valid(row, col + 1):
                    process.append((row, col + 1))
            dfs(process)

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

