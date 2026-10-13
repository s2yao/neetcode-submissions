class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        curr = []
        ret = []
        visited = [False] * (len(nums) + 1)

        def backtrack(length):
            if length == len(nums):
                ret.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    continue
                
                visited[i] = True
                curr.append(nums[i])
                backtrack(length + 1)
                curr.pop()
                visited[i] = False

        backtrack(0)
        return ret