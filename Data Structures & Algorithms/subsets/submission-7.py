class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        curr = []

        def dfs(curr_level):
            if curr_level == len(nums):
                ret.append(curr.copy())
                return
            curr.append(nums[curr_level])
            dfs(curr_level + 1)
            curr.pop()
            dfs(curr_level + 1)

        dfs(0)
        return ret