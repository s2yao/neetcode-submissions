class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        curr = []

        def backtrack(idx):
            ret.append(curr.copy())
            
            for i in range(idx, len(nums)):
                curr.append(nums[i])
                backtrack(i + 1)
                curr.pop()

        
        backtrack(0)
        return ret
        

