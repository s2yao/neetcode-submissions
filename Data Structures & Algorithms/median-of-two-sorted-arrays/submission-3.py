class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findKth(k: int):
            # keep track of removal progress
            nums1_curr_start_idx = 0
            nums2_curr_start_idx = 0

            while True:
                # if one array went out of bound
                # the other array + removal count contains only potential k
                if len(nums1) == nums1_curr_start_idx:
                    return nums2[nums2_curr_start_idx + k - 1]
                if len(nums2) == nums2_curr_start_idx:
                    return nums1[nums1_curr_start_idx + k - 1]
                if k == 1: return min(nums1[nums1_curr_start_idx], nums2[nums2_curr_start_idx])
                
                potential_k = k // 2

                new_nums1_potential_k = min(len(nums1), potential_k + nums1_curr_start_idx) - 1
                new_nums2_potential_k = min(len(nums2), potential_k + nums2_curr_start_idx) - 1

                nums1_potential_k = nums1[new_nums1_potential_k]
                nums2_potential_k = nums2[new_nums2_potential_k]

                if nums1_potential_k <= nums2_potential_k:
                    removed = new_nums1_potential_k - nums1_curr_start_idx + 1
                    nums1_curr_start_idx = new_nums1_potential_k + 1
                    k -= removed
                else:
                    removed = new_nums2_potential_k - nums2_curr_start_idx + 1
                    nums2_curr_start_idx = new_nums2_potential_k + 1
                    k -= removed

        # 1 indexed
        # if odd, median at len(nums1) + len(nums2) // 2 + 1
        if (len(nums1) + len(nums2)) % 2 == 1:
            return findKth((len(nums1) + len(nums2)) // 2 + 1)

        # even median at len(nums1) + len(nums2) // 2 (+1)
        left = findKth((len(nums1) + len(nums2)) // 2)
        right = findKth((len(nums1) + len(nums2)) // 2 + 1)

        return (left + right) / 2
