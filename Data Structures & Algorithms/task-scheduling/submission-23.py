import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_heap = []

        count = Counter(tasks)

        for occ in count.values():
            heapq.heappush(max_heap, -occ)

        ret = 0
        
        while max_heap:
            put_back = []
            curr_steps = 0

            for _ in range(n + 1):
                if not max_heap:
                    break
                
                curr_occ = heapq.heappop(max_heap)
                # print(curr_occ)
                curr_occ += 1
                if curr_occ < 0:
                    put_back.append(curr_occ)
                curr_steps += 1
            
            for ele in put_back:
                heapq.heappush(max_heap, ele)
            
            if not max_heap:
                ret += curr_steps
            else:
                ret += n + 1
        
        return ret