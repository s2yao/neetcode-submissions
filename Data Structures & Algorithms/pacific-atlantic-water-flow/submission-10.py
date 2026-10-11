class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = []
        atlantic = []

        # find all init cell for pacific
        for row in range(len(heights)):
            pacific.append((row, 0))
        for col in range(len(heights[0])):
            pacific.append((0, col))
        pacific_set = set(pacific)

        # find all init cell for atlantic
        for row in range(len(heights)):
            atlantic.append((row, len(heights[0]) - 1))
        for col in range(len(heights[0])):
            atlantic.append((len(heights) - 1, col))
        atlantic_set = set(atlantic)

        def check_valid(row, col, prev_height):
            if row < 0 or col < 0 or row >= len(heights) or col >= len(heights[0]):
                return False
            curr_height = heights[row][col]
            if curr_height < prev_height:
                return False
            return True

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        # function that does a dfs into every cell walkable
        def traversal(ocean_posn, ocean_set):
            
            while ocean_posn:
                row, col = ocean_posn.pop()
                
                for dr, dc in directions:
                    probe_row, probe_col = row + dr, col + dc
                    if not check_valid(probe_row, probe_col, heights[row][col]) or (probe_row, probe_col) in ocean_set:
                        continue
                    ocean_set.add((probe_row, probe_col))
                    ocean_posn.append((probe_row, probe_col))
        
        traversal(pacific, pacific_set)
        traversal(atlantic, atlantic_set)

        ret = []

        # for loop finding all element in both set
        for posn in pacific_set:
            if posn in atlantic_set:
                ret.append([posn[0], posn[1]])

        return ret
        