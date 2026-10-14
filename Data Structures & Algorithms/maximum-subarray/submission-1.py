class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        ret = float('-inf')

        for i in range(len(nums)):
            if curr_sum + nums[i] < 0:
                ret = max(ret, curr_sum + nums[i])
                curr_sum = 0
                continue
            
            curr_sum += nums[i]
            ret = max(ret, curr_sum)

        return ret
# -2, 3, -5