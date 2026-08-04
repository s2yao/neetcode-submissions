class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        house1 = 0
        house2 = 0
        curr = 0

        for house in range(1, len(nums)):
            curr = max(house2 + nums[house], house1)
            print(curr)
            house2 = house1
            print(house1)
            print(house2)
            house1 = curr


        house1 = 0
        house2 = 0
        curr2 = 0
        for house in range(len(nums) - 1):
            curr2 = max(house2 + nums[house], house1)
            house2 = house1
            house1 = curr2
        
        return max(curr, curr2)
