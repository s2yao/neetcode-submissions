class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        freq = [[] for _ in range(len(nums) + 1)]

        for ele, occ in count.items():
            freq[occ].append(ele)
        
        ret = []
        for i in reversed(range(len(freq))):
            curr_occ = freq[i]
            for j in reversed(range(len(curr_occ))):
                if len(ret) == k:
                    break
                ret.append(curr_occ[j])
        
        return ret