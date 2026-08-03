from collections import defaultdict 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for ele in nums:
            count[ele] += 1
    
        arr = [(x,y) for x, y in count.items()]

        arr.sort(key = lambda x: x[1])
        print(arr)

        return [arr[x][0] for x in range(len(arr))][len(arr) - k:]