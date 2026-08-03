class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for j in reversed(range(num, target + 1)):
                dp[j] = dp[j] or dp[j - num]
        
        return dp[target]






        # total_remain = sum(nums)
        # if total_remain % 2 == 1:
        #     return False

        # def dfs(curr_remain, arr):
        #     if curr_remain == total_remain // 2:
        #         return True
        #     if not arr or curr_remain > total_remain // 2:
        #         return False
        #     for idx in range(len(arr)):
        #         next_arr = arr[:idx] + arr[idx+1:]
        #         result = dfs(curr_remain + arr[idx], next_arr)
        #         if result:
        #             return result
        #     return False
        # return dfs(0, nums)