from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])

        for i in range(1, len(nums)):
            if dp[-1] < nums[i]:
                dp.append(nums[i])
                continue

            idx = bisect_left(dp, nums[i])
            dp[idx] = nums[i]

        return len(dp)