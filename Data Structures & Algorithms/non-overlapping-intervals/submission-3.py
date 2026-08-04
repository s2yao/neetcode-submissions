class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        ret = 0

        end = intervals[0][1]

        for idx in range(1, len(intervals)):
            curr_start = intervals[idx][0]
            curr_end = intervals[idx][1]
            # check if same end
            if curr_end == end:
                ret += 1
            # if not same end, we must have bigger end
            elif curr_start < end: # current interval overlapping
                ret += 1
            else:
                end = curr_end
            

        return ret

# case 1 - non overlap
# [1,2][2,3][3,4]
# ret = 0
# 3

# case 2 - overlap
# [1,2][1,4][3,4]
# ret = 1
# 4
# 34

# case 3 - same end\
# [15,25,35,45]
# ret = 3
# 5
# 25