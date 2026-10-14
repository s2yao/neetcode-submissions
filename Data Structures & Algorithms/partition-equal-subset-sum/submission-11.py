class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = total // 2

        def backtrack(idx, curr_sum):
            if curr_sum == target:
                return True
            if curr_sum > target:
                return False
            if idx == len(nums):
                return False
            
            if backtrack(idx + 1, curr_sum + nums[idx]) or backtrack(idx + 1, curr_sum):
                return True
            return False
            
        return backtrack(0, 0)