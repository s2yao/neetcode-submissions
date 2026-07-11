class MedianFinder:

    def __init__(self):
        self.upperheap_min = []
        self.lowerheap_max = []

        # need a way to keep track of middle element


    def addNum(self, num: int) -> None:
        # decides which heap it belongs to
        if self.upperheap_min and num > self.upperheap_min[0]:
            heapq.heappush(self.upperheap_min, num)
        else:
            heapq.heappush(self.lowerheap_max, -num)
        
        # balances the length of 2 heap by +- 1
        while abs(len(self.upperheap_min) - len(self.lowerheap_max)) > 1:
            if len(self.upperheap_min) > len(self.lowerheap_max):
                temp = heapq.heappop(self.upperheap_min)
                heapq.heappush(self.lowerheap_max, -temp)
            else:
                temp = heapq.heappop(self.lowerheap_max)
                heapq.heappush(self.upperheap_min, -temp)

    def findMedian(self) -> float:
        ret = 0
        if len(self.lowerheap_max) == len(self.upperheap_min):
            ret = (-self.lowerheap_max[0] + self.upperheap_min[0]) / 2
        elif len(self.lowerheap_max) > len(self.upperheap_min):
            ret = -self.lowerheap_max[0]
        else:
            ret = self.upperheap_min[0]

        return ret