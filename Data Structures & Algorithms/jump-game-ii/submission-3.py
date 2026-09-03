class Solution:
    def jump(self, nums: List[int]) -> int:
        # we dont care about last element

        # idx = 0 always true

        dp = [0] * len(nums)

        i = 0
        while i < (len(nums) - 1):
            jump = nums[i]
            dp[i] += 1
            # mark all possible jumps
            for j in range(i + 1, i + jump + 1):
                if j == len(nums):
                    break
                if dp[j] == 0:
                    dp[j] = dp[i]
                else:
                    dp[j] = min(dp[j], dp[i])
        
            i += 1
        
        return dp[-1]