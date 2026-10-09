class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def select(left, right):
            pivot = nums[right]
            slow = left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[i], nums[slow] = nums[slow], nums[i]
                    slow += 1
            nums[slow], nums[right] = nums[right], nums[slow]

            if slow == k:
                return nums[slow]
            elif slow > k:
                return select(left, slow - 1)
            else:
                return select(slow + 1, right)
        
        return select(0, len(nums) - 1)