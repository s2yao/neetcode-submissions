class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # keep track of curr_max and min
        curr_max = nums[0]
        curr_min = nums[0]
        ret = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            prev_max = curr_max
            curr_max = max(num, num * curr_min, num * curr_max)
            curr_min = min(num, num * curr_min, num * prev_max)
            ret = max(ret, curr_max, curr_min)

        return ret
