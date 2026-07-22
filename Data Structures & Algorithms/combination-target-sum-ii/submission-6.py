class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort() # nlong timsort
        ret = []

        def dfs(start, curr_sum, arr):
            if curr_sum == target:
                ret.append(arr)
                return
            if curr_sum > target:
                return
            
            for idx in range(start, len(candidates)):
                if idx > start and candidates[idx - 1] == candidates[idx]: # never fails
                    continue
                curr_ele = candidates[idx]
                # if element appear before
                dfs(idx + 1, curr_sum + curr_ele, arr + [curr_ele])
                


        dfs(0, 0, [])
        return ret

