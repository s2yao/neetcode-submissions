class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()

        sorted_queries = sorted((q, idx) for idx, q in enumerate(queries))

        min_heap = []
        res = [-1] * len(queries)
        interval_ptr = 0

        for q, idx in sorted_queries:
            while interval_ptr < len(intervals) and intervals[interval_ptr][0] <= q:
                start, end = intervals[interval_ptr]
                heapq.heappush(min_heap, (end - start + 1, end))
                interval_ptr += 1

            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            if min_heap:
                res[idx] = min_heap[0][0]

        return res