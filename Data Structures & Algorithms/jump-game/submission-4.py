class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        dp = [False] * (len(nums))
        dp[0] = True
        
        i = 0

        while i < len(nums) - 1:
            jump = nums[i]
            # curr jump with no possible jump to later
            if jump == 0 and not dp[i + 1]:
                return False
            
            # mark all possible jump
            j = i
            while j <= i + jump:
                if j == (len(nums) - 1):
                    return True
                dp[j] = True
                j += 1
            i += 1
        
        return dp[-1]