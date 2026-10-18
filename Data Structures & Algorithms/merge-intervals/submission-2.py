class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        curr_start = intervals[0][0]
        curr_end = intervals[0][1]
        ret = []

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if start <= curr_end:
                curr_start = min(curr_start, start)
                curr_end = max(curr_end, end)
            else:
                ret.append([curr_start, curr_end])
                curr_start = start
                curr_end = end
        ret.append([curr_start, curr_end])

        return ret