class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        ret = []
        merged_start = newInterval[0]
        merged_end = newInterval[1]
        for index in range(len(intervals)):
            curr_int_start = intervals[index][0]
            curr_int_end = intervals[index][1]
            # case1 new interval start after curr interval end
            # case2 interval overlap: update merged_interval
            # case3 2 intervals unrelated: 
            if merged_start > curr_int_end:
                ret.append([curr_int_start, curr_int_end])
            elif merged_end < curr_int_start:
                ret.append([merged_start, merged_end])
                return ret + intervals[index:]
            else: 
                merged_start = min(merged_start, curr_int_start)
                merged_end = max(merged_end, curr_int_end)
        
        ret.append([merged_start, merged_end])
        return ret

# intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]
# merged_start = 6
# merged_end = 7

