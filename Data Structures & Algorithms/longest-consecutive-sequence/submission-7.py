class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we iterate through the nums
        # and locate the "chain of consecutive"
        if len(nums) == 0: return 0

        nums_set = set(nums)
        ret = 1

        for curr_num in nums:
            if curr_num not in nums_set:
                continue

            curr_chain_count = 1
            # auto discard current one in the chain
            nums_set.discard(curr_num)

            # look up
            i = 1
            while (curr_num + i) in nums_set:
                # if found, discard
                nums_set.discard(curr_num + i)
                curr_chain_count += 1
                i += 1
            
            # look down
            i = 1
            while (curr_num - i) in nums_set:
                # if found, discard
                nums_set.discard(curr_num - i)
                curr_chain_count += 1
                i += 1
            
            ret = max(ret, curr_chain_count)

        return ret