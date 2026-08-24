class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 == 1:
            return False
        
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for ele in nums:
            for i in reversed(range(ele, len(dp))):
                dp[i] = dp[i] or dp[i - ele]
        return dp[-1]