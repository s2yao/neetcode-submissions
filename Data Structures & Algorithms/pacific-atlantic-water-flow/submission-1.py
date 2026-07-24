class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ret = []

        # pacific check
        def pacific(row, col):
            return (row == 0 or col == 0)

        # atlantic check
        def atlantic(row, col):
            return (col == len(heights[0]) - 1 or row == len(heights) - 1)

        # check whether the current cell can let water flow
        # and its valid
        def check_cell(curr_height, probe_row, probe_col):
            if not(0 <= probe_row < len(heights) and 0 <= probe_col < len(heights[0])):
                return False
            return curr_height >= heights[probe_row][probe_col]

        # conducts dfs until both ocean found
        def dfs(process):
            visited = set(process)
            pacific_found = False
            atlantic_found = False

            while process:
                curr_row, curr_col = process.pop()
                # cond for pacific
                curr_pacific = pacific(curr_row, curr_col)
                if curr_pacific:
                    pacific_found = True
                # cond for atlantic
                curr_atlantic = atlantic(curr_row, curr_col)
                if curr_atlantic:
                    atlantic_found = True
                if pacific_found and atlantic_found:
                    return True

                directions = [(curr_row + 1, curr_col), (curr_row - 1, curr_col), (curr_row, curr_col + 1), (curr_row, curr_col - 1)]
                curr_height = heights[curr_row][curr_col]

                for direction in directions:
                    probe_row, probe_col = direction
                    if not check_cell(curr_height, probe_row, probe_col):
                        continue
                    if (probe_row, probe_col) not in visited:
                        process.append((probe_row, probe_col))
                        visited.add((probe_row, probe_col))
            return False
        for row in range(len(heights)):
            for col in range(len(heights[0])):
                if dfs([(row, col)]):
                    ret.append([row, col])
        return ret
