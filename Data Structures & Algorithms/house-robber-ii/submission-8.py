class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        house1 = max(nums[0], nums[1])
        house2 = nums[0]
        ret1 = house1

        for i in range(2, len(nums) - 1):
            ret1 = max(house1, nums[i] + house2)
            house2 = house1
            house1 = ret1
        

        house1 = max(nums[1], nums[2])
        house2 = nums[1]
        ret2 = house1

        for i in range(3, len(nums)):
            ret2 = max(house1, nums[i] + house2)
            house2 = house1
            house1 = ret2
        
        return max(ret1, ret2)