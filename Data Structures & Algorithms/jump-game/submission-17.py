class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        furthest = 0
        for idx in range(len(nums)):
            jump = nums[idx]
            if idx > furthest:
                return False

            curr = idx + jump
            furthest = max(furthest, curr)
        
        return True