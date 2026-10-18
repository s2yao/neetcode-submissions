import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        queries = sorted([[start, original_idx] for original_idx, start in enumerate(queries)])
        
        interval_idx = 0

        min_heap = []

        ret = [-1] * len(queries)

        
        for target_start, ret_idx in queries:

            while interval_idx < len(intervals) and intervals[interval_idx][0] <= target_start:
                curr_interval = intervals[interval_idx]
                heapq.heappush(min_heap, [curr_interval[1] - curr_interval[0] + 1, curr_interval[1]])
                interval_idx += 1
            
            while min_heap and min_heap[0][1] < target_start:
                heapq.heappop(min_heap)
            
            if min_heap:
                ret[ret_idx] = min_heap[0][0]
            

        return ret