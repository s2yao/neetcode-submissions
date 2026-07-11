class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]

        for ele in nums:
            ret += [curr_lst + [ele] for curr_lst in ret]

        return ret