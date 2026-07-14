class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ret = []
        def dfs(start, curr_sum, curr_arr):
            if curr_sum > target:
                return
            elif curr_sum == target:
                self.ret.append(curr_arr)
                return
            for idx in range(start, len(nums)):
                dfs(idx, curr_sum + nums[idx], curr_arr + [nums[idx]])

        dfs(0, 0, [])
        return self.ret