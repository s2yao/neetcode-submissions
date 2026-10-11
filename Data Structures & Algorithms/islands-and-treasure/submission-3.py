class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        treasures = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    treasures.append([row, col])
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        layers = 1
        
        def check_valid(row, col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != inf:
                return False
            return True

        while treasures:
            curr_len = len(treasures)
            for _ in range(curr_len):
                curr_row, curr_col = treasures.popleft()
                
                for dr, dc in directions:
                    probe_row, probe_col = dr + curr_row, dc + curr_col
                    if not check_valid(probe_row, probe_col):
                        continue
                    treasures.append((probe_row, probe_col))
                    grid[probe_row][probe_col] = layers
            layers += 1


