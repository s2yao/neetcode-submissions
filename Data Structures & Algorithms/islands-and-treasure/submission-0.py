class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visited = set()        
        inf = 2147483647
        def check(row, col):
            # valid
            if row < 0 or col < 0 or row > len(grid) - 1 or col > len(grid[0]) - 1:
                return False
            # collision and in not inf
            if (row, col) in visited or grid[row][col] != inf:
                return False
            return True

        # muti point bfs
        def bfs(process):    
            curr_step = 0
            while process:
                next_layer = []
                curr_step += 1
                for treasure_row, treasure_col in process:
                    directions = [(treasure_row + 1, treasure_col), (treasure_row - 1, treasure_col), (treasure_row, treasure_col + 1), (treasure_row, treasure_col - 1)]
                    for probe_row, probe_col in directions:
                        if not check(probe_row, probe_col):
                            continue
                        # process
                        visited.add((probe_row, probe_col))
                        next_layer.append((probe_row, probe_col))
                        grid[probe_row][probe_col] = curr_step
                process = next_layer


        process = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    visited.add((row, col))
                    process.append((row, col))

        bfs(process)
