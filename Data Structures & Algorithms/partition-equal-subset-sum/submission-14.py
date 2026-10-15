class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 == 1:
            return False
        
        target = total // 2

        def backtrack(idx, curr_sum):
            if curr_sum > target:
                return False
            if curr_sum == target:
                return True
            
            for i in range(idx, len(nums)):
                if backtrack(i + 1, curr_sum + nums[idx]):
                    return True
        
            return False
        
        return backtrack(0, 0)
