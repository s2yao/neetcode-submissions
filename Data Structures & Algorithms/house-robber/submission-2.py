class Solution:
    def rob(self, nums: List[int]) -> int:
        accumulation1 = 0
        accumulation2 = 0

        for house in nums:
            curr_house = max(accumulation1, accumulation2 + house)
            accumulation2 = accumulation1
            accumulation1 = curr_house
        
        return accumulation1
        