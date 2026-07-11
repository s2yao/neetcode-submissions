from collections import deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        # use a heap to store only occurrence
        # heap records the current elements await process
        heap = [-counter for counter in count.values()]
        heapq.heapify(heap)

        # a queue to record the current cycle length
        queue = deque()
        ret_time = 0

        while heap or queue:
            ret_time += 1
            # if current CPU cycle is finish
            if ret_time > 1 and (ret_time - 1) % (n + 1) == 0:
                for ele in queue:
                    if ele:
                        heapq.heappush(heap, ele)
                queue = []

            # if no more tasks can be processed
            if not heap:
                queue.append(0)
                continue
            else:
                curr_ele_occur = heapq.heappop(heap) + 1
                if curr_ele_occur:
                    queue.append(curr_ele_occur)
                
        return ret_time