class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # keep track what is rotten
        rotten_set = set()
        # keep track total fruites
        fruit = 0
        # seed them
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fruit += 1
                if grid[row][col] == 2:
                    rotten_set.add((row, col))
                    fruit += 1
        
        # compute time it takes to maximize rotting
        def compute_time() -> int:
            # next_rotten contains all fruit that will be rotten
            next_rotten = list(rotten_set)
            minute = 0

            while next_rotten:
                new_rotten = []
                for rot_fruit in next_rotten:
                    row, col = rot_fruit
                    directions = [(row - 1, col), (row, col - 1), (row + 1, col), (row, col + 1)]
                    for direction in directions:
                        probe_row, probe_col = direction
                        if probe_row < 0 or probe_row > len(grid) - 1 or probe_col < 0 or probe_col > len(grid[0]) - 1:
                            continue
                        if grid[probe_row][probe_col] == 1 and (probe_row, probe_col) not in rotten_set:
                            new_rotten.append((probe_row, probe_col))
                            rotten_set.add((probe_row, probe_col))
                next_rotten = new_rotten
                if new_rotten:
                    minute += 1
            return minute

        time = compute_time()
        if len(rotten_set) == fruit:
            return time
        else:
            return -1




