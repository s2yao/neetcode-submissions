class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret = [1] * len(nums)

        pref = 1
        for i in range(len(nums)):
            ret[i] *= pref
            pref *= nums[i]

        suff = 1
        for i in reversed(range(len(nums))):
            ret[i] *= suff
            suff *= nums[i]

        return ret