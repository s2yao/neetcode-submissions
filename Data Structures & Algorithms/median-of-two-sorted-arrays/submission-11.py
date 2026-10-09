class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        total_len = len(nums1) + len(nums2)
        window = (total_len + 1) // 2
        # print(window)
        left = 0
        right = len(nums1)

        while True:
            guess1 = (left + right) // 2
            guess2 = window - guess1
            
            nums1_left = nums1[guess1 - 1] if guess1 - 1 >= 0 else float('-inf')
            print(guess1)
            nums1_right = nums1[guess1] if guess1 < len(nums1) else float('inf')
            # print(guess2)
            nums2_left = nums2[guess2 - 1] if guess2 - 1 >= 0 else float('-inf')
            nums2_right = nums2[guess2] if guess2 < len(nums2) else float('inf')
            # print(nums1_left, nums1_right)
            # print(nums2_left, nums2_right)
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if total_len % 2 == 0:
                    return ((max(nums1_left, nums2_left) + min(nums1_right, nums2_right))) / 2
                return max(nums1_left, nums2_left)
            
            if nums1_left > nums2_right:
                right = guess1 - 1
            else:
                left = guess1 + 1