import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        # can end with length 0 or 1
        while len(max_heap) > 1:
            stone1 = -heapq.heappop(max_heap)
            stone2 = -heapq.heappop(max_heap)
        
            # collide
            if stone1 != stone2:
                heapq.heappush(max_heap, -abs(stone1 - stone2))
            
        return -max_heap[0] if (len(max_heap) == 1) else 0