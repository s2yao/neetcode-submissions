class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        # pass 1 find the split point
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                # current mid to right inc
                right = mid
            else:
                left = mid + 1
        

        # idx left == right == smallest element
        if left != 0 and target >= nums[0] and target <= nums[left - 1]:
            new_left = 0
            new_right = left - 1
        else:
            new_left = left
            new_right = len(nums) - 1

        while new_left <= new_right:
            new_mid = (new_left + new_right) // 2
            if nums[new_mid] == target:
                return new_mid
            elif nums[new_mid] < target:
                new_left = new_mid + 1
            else:
                new_right = new_mid - 1
        
        return -1