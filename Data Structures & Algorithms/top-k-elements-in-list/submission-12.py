from collections import defaultdict 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for i in range((len(nums) + 1))]

        for num in nums:
            count[num] += 1
        
        for val, ct in count.items():
            freq[ct].append(val)

        ret = []
        for i in reversed(range(len(freq))):
            for val in freq[i]:
                ret.append(val)
                if len(ret) == k:
                    return ret