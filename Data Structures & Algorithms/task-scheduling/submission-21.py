import heapq
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        max_heap = [-val for val in count.values()]
        ret = 0
        
        while max_heap:
            last_cycle_count = 0
            putback = []
            for _ in range(n + 1):
                if not max_heap:
                    break
                curr_pop = heapq.heappop(max_heap)
                last_cycle_count += 1
                curr_pop += 1
                if curr_pop < 0:
                    putback.append(curr_pop)
            
            for ele in putback:
                heapq.heappush(max_heap, ele)
            
            if not max_heap:
                ret += last_cycle_count
            else:
                ret += (n + 1)
        
        return ret