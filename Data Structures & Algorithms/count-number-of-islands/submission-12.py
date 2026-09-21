class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # visited = set()
        # updating the current posn of the grid = 0
        ret = 0

        # checks if current posn is a land
        def check(row, col) -> bool:
            # its not out of bound
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return False
            # this posn is a land
            if grid[row][col] == '0':
                return False
            return True

        # dfs for 4 directions
        def dfs(row, col) -> None:
            # checking if current posn is island
            if not check(row, col):
                return False
            # update the current land to 0
            grid[row][col] = '0'

            # recursively look in 4 direction
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if check(row, col):
                    dfs(row, col)
                    ret += 1
        return ret
        