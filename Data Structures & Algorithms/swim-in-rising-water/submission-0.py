class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        min_heap = [[grid[0][0], 0, 0]]

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        # return true if current posn unvisited, inbound
        def check_valid(row, col) -> bool:
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return False
            if grid[row][col] == -1:
                return False
            return True

        ret = grid[0][0]
        while min_heap:
            curr_height, curr_row, curr_col = heapq.heappop(min_heap)
            grid[curr_row][curr_col] = -1
            ret = curr_height
            if curr_row == len(grid) - 1 and curr_col == len(grid[0]) - 1:
                return ret
            for dr, dc in directions:
                probe_row, probe_col = dr + curr_row, dc + curr_col
                if not check_valid(probe_row, probe_col):
                    continue
                # add posn new weight
                heapq.heappush(min_heap, [max(curr_height, grid[probe_row][probe_col]), probe_row, probe_col])
                # mark visited
                grid[probe_row][probe_col] = -1
        
