class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        furthest = 0
        for idx, jump in enumerate(nums[:len(nums) - 1]):
            if idx > furthest:
                return False

            curr = idx + jump
            furthest = max(furthest, curr)
            print(curr, furthest)
            if furthest >= len(nums) - 1:
                return True
        
        return False