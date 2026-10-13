class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        curr = []
        ret = []
        
        def backtrack(idx, curr_sum):
            if curr_sum > target:
                return
            if curr_sum == target:
                ret.append(curr.copy())
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                
                curr.append(candidates[i])
                backtrack(i + 1, curr_sum + candidates[i])
                curr.pop()

        backtrack(0, 0) 
        return ret