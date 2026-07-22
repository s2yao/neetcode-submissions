class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        # dict = {ele: set(idxes)}
        curr_comb = defaultdict(set)

        def dfs(curr_arr):
            if len(curr_arr) == len(nums):
                ret.append(curr_arr)
                return

            for idx in range(len(nums)):
                # curr element appeared before
                curr_ele = nums[idx]
                if (curr_ele in curr_comb) and idx in curr_comb[curr_ele]:
                    continue

                # add idx
                curr_comb[curr_ele].add(idx)

                dfs(curr_arr + [curr_ele])

                # discard idx from set
                curr_comb[curr_ele].discard(idx)
                # discard ele from set
                if len(curr_comb[curr_ele]) == 0:
                    del curr_comb[curr_ele]
                
        dfs([])
        return ret