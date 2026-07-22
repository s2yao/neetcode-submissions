class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        # dict = {ele: idx}
        curr_comb = defaultdict(int)

        def dfs():
            if len(curr_comb) == len(nums):
                # todo: convert to appendables
                temp = []
                for key in curr_comb:
                    temp.append(key)
                ret.append(temp)
                return

            for idx in range(len(nums)):
                # curr element appeared before
                curr_ele = nums[idx]
                if (curr_ele in curr_comb):
                    continue

                curr_comb[curr_ele] = idx

                dfs()

                # discard ele from set
                del curr_comb[curr_ele]
                
        dfs()
        return ret