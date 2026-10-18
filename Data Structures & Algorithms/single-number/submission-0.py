class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        fuck = 0
        for num in nums:
            fuck ^= num
        return fuck