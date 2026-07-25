class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_set = set()
        atlantic_set = set()
        ret = []
        visiting = set()

        # adds all blocks that can be visited by starting with posn
        # goes to land thats higher than current land
        def dfs(r, c, ocean):
            if ocean == 'p':
                if (r, c) not in pacific_set:
                    pacific_set.add((r, c))
                else:
                    return
            elif ocean == 'a':
                if (r, c) not in atlantic_set:
                    atlantic_set.add((r, c))
                else:
                    return
            curr_height = heights[r][c]

            directions = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
            
            for probe_row, probe_col in directions:
                if probe_row < 0 or probe_col < 0 or probe_row > len(heights) - 1 or probe_col > len(heights[0]) - 1:
                    continue
                probe_height = heights[probe_row][probe_col]
                # not visited and and height > curr_height
                if curr_height <= probe_height and (probe_row, probe_col) not in visiting:
                    visiting.add((probe_row, probe_col))
                    dfs(probe_row, probe_col, ocean)
                    visiting.discard((probe_row, probe_col))

        # iteration through all the cells
        for col in range(len(heights[0])):
            visiting.add((0, col))
            dfs(0, col, "p")
            visiting.discard((0, col))
            
            visiting.add((len(heights) - 1, col))
            dfs(len(heights) - 1, col, "a")
            visiting.discard((len(heights) - 1, col))

        for row in range(len(heights)):
            visiting.add((row, 0))
            dfs(row, 0, "p")
            visiting.discard((row, 0))
            visiting.add((row, len(heights[0]) - 1))
            dfs(row, len(heights[0]) - 1, "a")
            visiting.discard((row, len(heights[0]) - 1))

        for ele in pacific_set:
            if ele in atlantic_set:
                ret.append(ele)
        
        return ret

# [[2,1],
#  [1,2]]
# pacific_set = (0, 0) (1, 1)
# atlantic_set = set()
# ret = []
# visiting = (0, 0)
# 1, 0
