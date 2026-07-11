class MedianFinder:

    def __init__(self):
        self.length = 0
        self.heap = []

        # need a way to keep track of middle element

    def addNum(self, num: int) -> None:
        heapq.heappush(self.heap, num)
        self.length += 1

    def findMedian(self) -> float:
        num_to_pop = (self.length + 1) // 2
        put_back_in = []
        for _ in range(num_to_pop):
            put_back_in.append(heapq.heappop(self.heap))
        print(num_to_pop)
        print(put_back_in)
        ret = 0
        if put_back_in:
            ret = put_back_in[-1]
            if self.length % 2 == 0:
                ele2 = heapq.heappop(self.heap)
                heapq.heappush(self.heap, ele2)
                ret = (ret + ele2) / 2

        
        # seed back
        for ele in put_back_in:
            heapq.heappush(self.heap, ele)

        return ret