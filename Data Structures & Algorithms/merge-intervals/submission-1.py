class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ret = []
        # sort to end
        intervals.sort()

        # define a start interval 
        curr_start = intervals[0][0]
        curr_end = intervals[0][1]
        if len(intervals) == 1:
            return [[curr_start, curr_end]]

        for idx in range(1, len(intervals)):
            interval = intervals[idx]
            if interval[0] > curr_end:
                ret.append([curr_start, curr_end])
                curr_start = interval[0]
                curr_end = interval[1]
            else:
                curr_start = min(curr_start, interval[0])
                curr_end = max(curr_end, interval[1])

        # if last 2 is merging op
        ret.append([curr_start, curr_end])

        return ret


