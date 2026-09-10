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

            while curr_i_ptr < len(intervals) and intervals[curr_i_ptr][0] <= curr_q:
                start, end = intervals[curr_i_ptr]
                heapq.heappush(min_heap, (end - start + 1, end))
                curr_i_ptr += 1

            while min_heap and min_heap[0][1] < curr_q:
                heapq.heappop(min_heap)

            if min_heap:
                for i in dict_posn[curr_q]:
                    ret[i] = min_heap[0][0]

            curr_q_ptr += 1
        
        return ret