class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []

        def backtrack(idx, curr_int):
            if idx == len(nums):
                ret.append(curr_int)
                return
            
            backtrack(idx + 1, curr_int + [nums[idx]])
            backtrack(idx + 1, curr_int)
        
        backtrack(0, [])
        return ret