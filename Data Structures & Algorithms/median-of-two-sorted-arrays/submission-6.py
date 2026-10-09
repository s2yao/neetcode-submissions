class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Binary search the shorter array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        left = 0
        right = len(nums1)
        total_len = len(nums1) + len(nums2)
        total_left = (total_len + 1) // 2

        while left <= right:
            # Number of elements on the left of each partition
            guess1 = (left + right) // 2
            guess2 = total_left - guess1

            # Partition boundaries for nums1
            if guess1 > 0:
                left_in = nums1[guess1 - 1]
            else:
                left_in = float("-inf")

            if guess1 < len(nums1):
                left_out = nums1[guess1]
            else:
                left_out = float("inf")

            # Partition boundaries for nums2
            if guess2 > 0:
                right_in = nums2[guess2 - 1]
            else:
                right_in = float("-inf")

            if guess2 < len(nums2):
                right_out = nums2[guess2]
            else:
                right_out = float("inf")

            # Check whether the partition is valid
            if left_in <= right_out and right_in <= left_out:
                if total_len % 2 == 0:
                    return (max(left_in, right_in) + min(left_out, right_out)) / 2

                return float(max(left_in, right_in))

            # Adjust the partition in nums1
            if left_in > right_out:
                right = guess1 - 1
            else:
                left = guess1 + 1