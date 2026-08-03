class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ret = 0

        def dfs(idx, curr_sum):
            nonlocal ret
            if idx == len(nums):
                if curr_sum == target:
                    ret += 1
                return
            
            dfs(idx + 1, curr_sum + nums[idx])
            dfs(idx + 1, curr_sum - nums[idx])

        dfs(0, 0)

        return ret
