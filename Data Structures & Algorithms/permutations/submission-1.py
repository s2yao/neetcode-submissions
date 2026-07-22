class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        # keep track of idxes that appeared before
        idx_appear = set()

        def dfs(curr_arr):
            if len(curr_arr) == len(nums):
                ret.append(curr_arr)
                return

            for idx in range(len(nums)):
                # curr idx appeared before
                if (idx in idx_appear):
                    continue

                # add idx to set
                idx_appear.add(idx)

                curr_ele = nums[idx]
                dfs(curr_arr + [curr_ele])

                # discard ele from set
                idx_appear.discard(idx)
                
        dfs([])
        return ret