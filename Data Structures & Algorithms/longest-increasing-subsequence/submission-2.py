from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        # record current 
        dp.append(nums[0])

        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
                continue
            
            # find the index to replace
            # return idx containing ele bigger than current ele
            idx = bisect_left(dp, nums[i])
            dp[idx] = nums[i]

        return len(dp)