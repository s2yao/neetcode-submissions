class Solution:
    def combinationSum2(
        self,
        candidates: List[int],
        target: int
    ) -> List[List[int]]:
        candidates.sort()
        ret = []

        def dfs(start: int, curr_sum: int, result: List[int]) -> None:
            if curr_sum == target:
                ret.append(result.copy())
                return

            for idx in range(start, len(candidates)):
                if idx > start and candidates[idx] == candidates[idx - 1]:
                    continue

                curr_ele = candidates[idx]

                if curr_sum + curr_ele > target:
                    break

                result.append(curr_ele)
                dfs(idx + 1, curr_sum + curr_ele, result)
                result.pop()

        dfs(0, 0, [])
        return ret