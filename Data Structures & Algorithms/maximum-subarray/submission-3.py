class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(dp)):
            dp[i] = max(nums[i] + dp[i-1], nums[i])
        
        print(dp)
        return max(dp)