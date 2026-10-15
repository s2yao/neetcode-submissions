class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ret = []
        curr = []

        def backtrack(idx):
            ret.append(curr.copy())
            
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                curr.append(nums[i])
                backtrack(i + 1)
                curr.pop()
        
        backtrack(0)
        return ret