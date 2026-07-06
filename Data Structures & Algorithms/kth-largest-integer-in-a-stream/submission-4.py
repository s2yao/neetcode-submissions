import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap_len = k
        self.heap = nums
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)


    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.heap_len:
            heapq.heappop(self.heap)

        return self.heap[0] 