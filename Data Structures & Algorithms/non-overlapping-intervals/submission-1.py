class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # every different end can only have 1 interval
        # others overlap
        
        # sort by end 
        intervals.sort(key = lambda x : x[1])
        curr_end = intervals[0][1]
        ret = 0
        for interval in intervals[1:]:
            if interval[0] < curr_end:
                ret += 1
            else:
                curr_end = interval[1]
        
        return ret