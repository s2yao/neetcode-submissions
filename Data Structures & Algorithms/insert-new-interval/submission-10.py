class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        curr_int_start = newInterval[0]
        curr_int_end = newInterval[1]
        
        ret = []

        for start, end in intervals:
            if curr_int_start > end:
                ret.append([start, end])
            elif end >= curr_int_start and start <= curr_int_end:
                curr_int_start = min(curr_int_start, start)
                curr_int_end = max(curr_int_end, end)
            else:
                ret.append([curr_int_start, curr_int_end])
                curr_int_start = start
                curr_int_end = end
        
        ret.append([curr_int_start, curr_int_end])
        return ret
