class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def search(start, remaining, path):
            if remaining == 0:
                result.append(path)
                return
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                number = candidates[i]

                if i > start and number == candidates[i - 1]:
                    continue

                search(i + 1, remaining - number, path + [number])

        search(0, target, [])
        return result