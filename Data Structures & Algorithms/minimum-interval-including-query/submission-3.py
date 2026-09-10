from collections import defaultdict
import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sort according to start
        intervals.sort(key = lambda x: x[0])

        # record queries original posn
        dict_posn = defaultdict(list)
        ret = [-1] * len(queries)
        for idx, val in enumerate(queries):
            dict_posn[val].append(idx)
        queries.sort()

        # min_heap for interval length
        min_heap = []

        # iterate according the queries
        curr_q_ptr = 0
        curr_i_ptr = 0
        while curr_q_ptr < len(queries):
            curr_q = queries[curr_q_ptr]
            # append all interval with start <= curr_q
            while curr_i_ptr < len(intervals) and intervals[curr_i_ptr][0] <= curr_q:
                heapq.heappush(min_heap, (intervals[curr_i_ptr][1] - intervals[curr_i_ptr][0] + 1, intervals[curr_i_ptr][1]))
                curr_i_ptr += 1

            # update curr_q
            # eliminate all interval with end < curr_q
            while min_heap and min_heap[0][1] < curr_q:
                heapq.heappop(min_heap)
            
            # if there remains interval
            if min_heap:
                for i in dict_posn[curr_q]:
                    ret[i] = min_heap[0][0]
            curr_q_ptr += 1
        
        return ret
