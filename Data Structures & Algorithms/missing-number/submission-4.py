class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        fuck = 0

        for num in nums:
            fuck ^= num
        
        for i in range(0, len(nums) + 1):
            fuck ^= i

        return fuck
        
            