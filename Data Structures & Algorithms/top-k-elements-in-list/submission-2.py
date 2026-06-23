class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_count = defaultdict(int)

        for ele in nums:
            dict_count[ele] += 1
        
        ret = []

        for key, value in dict_count.items():
            ret.append((value, key))

        ret.sort(reverse=True)

        ret_ret = []

        for i in range(k):
            ret_ret.append(ret[i][1])
        
        return ret_ret