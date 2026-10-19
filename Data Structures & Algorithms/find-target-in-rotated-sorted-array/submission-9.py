class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            curr_mid = nums[mid]

            if curr_mid == target:
                return mid
            if curr_mid < nums[right]:
                if curr_mid < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target < curr_mid:
                    right = mid - 1
                else:
                    left = mid + 1
            

        return -1

