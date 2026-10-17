from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        @cache
        def dfs_backtrack(left, right):
            if left > right:
                return 0
            
            curr_max = 0
            for i in range(left, right + 1):
                coin = nums[i] * nums[left - 1] * nums[right + 1]
                left_coin = dfs_backtrack(left, i - 1)
                right_coin = dfs_backtrack(i + 1, right)
                curr_max = max(curr_max, coin + left_coin + right_coin)
            return curr_max

        return dfs_backtrack(1, len(nums) - 2)