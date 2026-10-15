class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret_arr = []
        curr = []

        def backtrack(idx, curr_sum):
            if curr_sum == target:
                ret_arr.append(curr.copy())
                return
            if curr_sum > target:
                return
            
            for i in range(idx, len(nums)):
                curr.append(nums[i])
                backtrack(i, curr_sum + nums[i])
                curr.pop()
        
        backtrack(0, 0)
        return ret_arr