class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        ret = float('-inf')
        for idx, num in enumerate(nums):
            curr_sum += num
            if curr_sum < 0:
                ret = max(ret, curr_sum)
                curr_sum = 0
                continue
            
            ret = max(ret, curr_sum)
        return ret