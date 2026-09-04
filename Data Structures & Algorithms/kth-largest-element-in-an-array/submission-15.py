class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def resolve_pivot(left, right):
            pivot = nums[right]
            ptr = left

            for i in range(left, right):
                if pivot < nums[i]:
                    nums[i], nums[ptr] = nums[ptr], nums[i]
                    ptr += 1
                
            nums[right], nums[ptr] = nums[ptr], nums[right]
            if ptr + 1 == k:
                return nums[ptr]
            elif ptr + 1 < k:
                return resolve_pivot(ptr + 1, right)
            else:
                return resolve_pivot(left, ptr - 1)


        return resolve_pivot(0, len(nums) - 1)