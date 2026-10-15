class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited_idx = [False] * len(nums)

        curr = []
        ret = []

        def backtrack(idx):
            if idx == len(nums):
                ret.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if visited_idx[i]:
                    continue
                
                visited_idx[i] = True
                curr.append(nums[i])
                backtrack(idx+1)
                visited_idx[i] = False
                curr.pop()

        backtrack(0)
        return ret