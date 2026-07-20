class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []

        def dfs(idx, curr_sum, arr):
            if curr_sum == target:
                ret.append(arr)
                return
            if curr_sum > target:
                return
            
            for idx in range(idx, len(nums)):
                dfs(idx, curr_sum + nums[idx], arr + [nums[idx]])

        dfs(0, 0, [])
        return ret