class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        # element put to a set first: On
        curr_set = set(nums)

        target_idx = 0
        ret_max = 1

        while curr_set and target_idx < len(nums):
            if nums[target_idx] not in curr_set:
                target_idx += 1
                continue

            curr_max = 1
            target_ele = nums[target_idx]
            curr_set.discard(target_ele)

            # while target element - 1 exist
            i = 1
            while (target_ele - i) in curr_set:
                # check for target element - 1 - 1 -..... until no more
                # if exist, take out of the set
                curr_set.discard(target_ele - i)
                # add 1 to curr_max
                curr_max += 1
                i += 1

            i = 1
            # while target element
            while (target_ele + i) in curr_set:
                # check for target element + 1 + 1 +..... until no more
                # if exist, take out of the set
                curr_set.discard(target_ele + i)
                # add 1 to curr_max
                curr_max += 1
                i += 1

            target_idx += 1
            ret_max = max(ret_max, curr_max)

        return ret_max