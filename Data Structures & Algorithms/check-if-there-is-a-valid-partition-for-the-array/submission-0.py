class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        two = nums[-1] == nums[-2]
        if len(nums) <= 2:
            return two
        three = (nums[-3] + 1 == nums[-2] == nums[-1] - 1) or (nums[-1] == nums[-2] == nums[-3])
        dp = [three, two, False]
        
        for i in reversed(range(len(nums) - 3)):
            two_equal = nums[i] == nums[i + 1]
            three_equal = nums[i] == nums[i + 1] == nums[i + 2]
            three_inc = nums[i] + 1 == nums[i + 1] == nums[i + 2] - 1

            res = (two_equal and dp[1]) or (three_equal and dp[2]) or (three_inc and dp[2])
            dp = [res, dp[0], dp[1]]

        
        return dp[0]