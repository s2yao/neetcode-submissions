class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # fuck ass solution
        # sort nums first and use 2 ptrs to locate valid result
        nums.sort()
        ret = []

        for idx1 in range(len(nums)):
            if idx1 != 0 and nums[idx1] == nums[idx1 - 1]:
                continue
            
            left = idx1 + 1
            right = len(nums) - 1

            while left < right:
                curr_result = nums[idx1] + nums[left] + nums[right]

                if curr_result == 0:
                    ret.append([nums[idx1], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif curr_result > 0:
                    right -= 1
                else:
                    left += 1
                
        return ret


nums = [-4, -1, -1, 0, 1, 2]
curr = -1
left = 0
right = 1

