class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fruit = 0
        rotten = deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fruit += 1
                if grid[row][col] == 2:
                    rotten.append([row, col])
        
        def check_valid(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != 1:
                return False
            return True
        ret = 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while rotten and fruit > 0:
            curr_len = len(rotten)
            ret += 1
            
            for _ in range(curr_len):
                curr_row, curr_col = rotten.popleft()
                for dr, dc in directions:
                    probe_row, probe_col = curr_row + dr, curr_col + dc
                    if not check_valid(probe_row, probe_col):
                        continue
                    fruit -= 1
                    grid[probe_row][probe_col] = 2
                    rotten.append([probe_row, probe_col])
        
        if fruit > 0:
            return -1
        return ret
