class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        ret = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            prev_max = curr_max
            prev_min = curr_min

            curr_max = max(num, num * prev_max, num * prev_min)
            curr_min = min(num, num * prev_max, num * prev_min)

            ret = max(ret, curr_max)

        return ret