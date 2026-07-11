class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]

        for num in nums:
            ret += [current_list + [num] for current_list in ret]

        return ret