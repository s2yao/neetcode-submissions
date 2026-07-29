class Solution:
    def rob(self, nums: List[int]) -> int:
        house1 = 0
        house2 = 0

        for money in nums:
            current = max(house2, house1 + money)
            house1 = house2
            house2 = current

        return house2