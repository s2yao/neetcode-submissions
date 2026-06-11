class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # setting a prefix and suffix to calculate

        pref = 1
        suff = 1
        ret = [1] * len(nums)

        # for loop from beginnning to end
        for i in range(len(nums)):
            ret[i] *= pref
            pref *= nums[i]

        # for loop from end to beginning
        for i in reversed(range(len(nums))):
            ret[i] *= suff
            suff *= nums[i]
        
        return ret