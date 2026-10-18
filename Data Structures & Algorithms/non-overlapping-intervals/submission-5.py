class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        curr_end = intervals[0][1]
        ret = 0
        print(intervals)
        for start, end in intervals[1:]:
            if end == curr_end:
                ret += 1
            elif start < curr_end:
                ret += 1
            else:
                curr_end = end

        return ret