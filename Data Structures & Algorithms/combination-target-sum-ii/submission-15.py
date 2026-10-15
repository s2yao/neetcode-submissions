class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        curr = []
        candidates.sort()

        def backtrack(idx, curr_sum):
            if curr_sum == target:
                ret.append(curr.copy())
                return
            if curr_sum > target:
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                
                curr.append(candidates[i])
                backtrack(i + 1, curr_sum + candidates[i])
                curr.pop()
        
        backtrack(0, 0)
                
        return ret