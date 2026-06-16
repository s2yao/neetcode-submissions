class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findKth(k: int) -> int:
            i = 0
            j = 0

            while True:
                if i == len(nums1):
                    return nums2[j + k - 1]

                if j == len(nums2):
                    return nums1[i + k - 1]

                if k == 1:
                    return min(nums1[i], nums2[j])

                eliminate = k // 2

                new_i = min(i + eliminate, len(nums1)) - 1
                new_j = min(j + eliminate, len(nums2)) - 1

                if nums1[new_i] <= nums2[new_j]:
                    removed = new_i - i + 1
                    i = new_i + 1
                    k -= removed
                else:
                    removed = new_j - j + 1
                    j = new_j + 1
                    k -= removed

        total = len(nums1) + len(nums2)

        if total % 2 == 1:
            return float(findKth(total // 2 + 1))

        left = findKth(total // 2)
        right = findKth(total // 2 + 1)

        return (left + right) / 2