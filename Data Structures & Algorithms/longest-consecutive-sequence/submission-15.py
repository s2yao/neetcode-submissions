class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ret = 0

        for num in num_set:
            # Only start counting from the beginning of a sequence
            if num - 1 in num_set:
                continue

            curr_max = 1
            probe_up = num

            # Expand until the sequence ends
            while probe_up + 1 in num_set:
                curr_max += 1
                probe_up += 1

            ret = max(ret, curr_max)

        return ret