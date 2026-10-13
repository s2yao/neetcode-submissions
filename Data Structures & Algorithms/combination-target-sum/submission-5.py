class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        curr_ele = []

        def backtrack(idx, curr_sum):
            if curr_sum > target:
                return
            if curr_sum == target:
                ret.append(curr_ele.copy())
                return
            
            for i in range(idx, len(nums)):
                curr_ele.append(nums[i])
                backtrack(i, curr_sum + nums[i])
                curr_ele.pop()
        
        backtrack(0, 0)
        return ret