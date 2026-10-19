class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = [False] * len(nums)

        ret = []
        curr = []
        def backtrack(idx):
            if idx == len(nums):
                ret.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    continue
                
                visited[i] = True
                curr.append(nums[i])
                backtrack(idx + 1)
                visited[i] = False
                curr.pop()
        
        backtrack(0)
        return ret