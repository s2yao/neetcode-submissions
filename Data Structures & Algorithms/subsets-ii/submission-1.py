class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []

        def dfs(start, curr_arr):
            for idx in range(start, len(nums)):
                if idx > start and nums[idx] == nums[idx - 1]:
                    continue

                curr_ele = nums[idx]
                dfs(idx + 1, curr_arr + [curr_ele])

            ret.append(curr_arr)

        dfs(0, [])
        return ret
