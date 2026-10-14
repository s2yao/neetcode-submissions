from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []

        for num in nums:
            # >= num
            idx = bisect_left(dp, num)

            if idx == len(dp):
                dp.append(num)
            elif dp[idx] == num:
                continue
            else:
                dp[idx] = num
        
        return len(dp)