from collections import defaultdict 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sort a dict
        count_dict = defaultdict(int)

        for ele in nums:
            count_dict[ele] += 1

        # sort the dict according to value
        sort_list = sorted(count_dict.items(), key=lambda x: x[1])

        return [x[0] for x in sort_list[len(sort_list) - k:]]