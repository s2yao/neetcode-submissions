class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = []
        # return index newInterval should be in
        def index_interval(target):
            left = 0
            right = len(intervals)

            while left < right:
                mid = (left + right) // 2
                curr_ele = intervals[mid][0]

                if curr_ele == target:
                    return mid
                elif curr_ele < target:
                    left = mid + 1
                else:
                    right = mid

            return left

        init_up_to = index_interval(newInterval[0])
        if init_up_to > 0 and intervals[init_up_to - 1][1] >= newInterval[0]:
            init_up_to -= 1
        for i in range(init_up_to):
            ret.append(intervals[i])
        
        def merger(start_idx):
            new_start = newInterval[0]
            new_end = newInterval[1]
            curr_idx = start_idx
            # breaks at idx of non-overlapping interval
            while curr_idx < len(intervals) and intervals[curr_idx][0] <= new_end:
                new_start = min(intervals[curr_idx][0], new_start)
                new_end = max(intervals[curr_idx][1], new_end)
                curr_idx += 1
            ret.append([new_start, new_end])
            return curr_idx
        
        merge_start = merger(init_up_to)

        for i in range(merge_start, len(intervals)):
            ret.append(intervals[i])
        
        return ret
