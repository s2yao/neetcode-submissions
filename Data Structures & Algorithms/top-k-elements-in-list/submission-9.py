import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_count = defaultdict(int)

        for ele in nums:
            dict_count[ele] += 1
        
        count_arr = [[] for i in range(len(nums) + 1)] # O(n)

        for key, value in dict_count.items():
            count_arr[value].append(key)

        ret = []
        for ele in reversed(count_arr):
            if len(ret) == k:
                return ret
            ret.extend(ele)