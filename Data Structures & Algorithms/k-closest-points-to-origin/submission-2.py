import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for point in points:
            pointx = point[0]
            pointy = point[1]
            distance = pointx * pointx + pointy * pointy
            heapq.heappush(min_heap, (distance, pointx, pointy))

        ret = []
        for _ in range(k):
            closest = heapq.heappop(min_heap)
            ret.append([closest[1], closest[2]])        
        return ret