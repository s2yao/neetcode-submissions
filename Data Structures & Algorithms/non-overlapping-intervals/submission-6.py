class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        ret = 0
        curr_end = intervals[0][1]

        for start, end in intervals[1:]:
            # if intervals have same end == overlap
            if end == curr_end:
                ret += 1
            # if start < prev end == overlap
            elif start < curr_end:
                ret += 1
            # otherwise its another interval
            else:
                curr_end = end
        
        return ret

