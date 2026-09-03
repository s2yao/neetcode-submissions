class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dont care about last idx jump
        # beginning always to True

        dp = [False] * len(nums)
        dp[0] = True

        for i in range(len(nums) - 1):
            curr_jump = nums[i]

            if curr_jump == 0 and not dp[i + 1]:
                return False
            
            # update possible jumps
            for j in range(i, i + curr_jump + 1):
                if j == len(nums) - 1:
                    return True
                dp[j] = True
        
        return dp[-1]