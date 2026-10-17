from functools import cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        @cache
        def dfs_backtrack(left, right):
            if left > right:
                return 0

            curr_max = 0

            # Try every balloon as the LAST balloon to burst
            for idx in range(left, right + 1):

                # Coins earned by bursting this balloon last
                left_balloon = nums[left - 1]
                right_balloon = nums[right + 1]
                curr_balloon = nums[idx]

                coins = left_balloon * curr_balloon * right_balloon

                # Burst all balloons on both sides first
                left_coins = dfs_backtrack(left, idx - 1)
                right_coins = dfs_backtrack(idx + 1, right)

                # Total coins for this choice
                total_coins = coins + left_coins + right_coins

                curr_max = max(curr_max, total_coins)

            return curr_max

        return dfs_backtrack(1, len(nums) - 2)