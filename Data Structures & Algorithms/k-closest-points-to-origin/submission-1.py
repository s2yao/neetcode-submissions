import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # min heap
        min_heap = []

        # seed max heap, idx as element
        for idx in range(len(points)):
            pointx = points[idx][0]
            pointy = points[idx][1]
            distance = math.sqrt(pointx * pointx + pointy * pointy)
            # store tuple(distance, fill?, idx)
            heapq.heappush(min_heap, (distance, idx))
        
        ret = []
        for _ in range(k):
            curr_tup = heapq.heappop(min_heap)
            ret.append(points[curr_tup[1]])
        
        return ret