class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        print(nums)

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            curr_num = nums[i]
            target_sum = -curr_num

            left = i + 1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum == target_sum:
                    ret.append([nums[i], nums[left], nums[right]])
                    print(nums[left + 1])
                    while left < len(nums) - 1 and nums[left + 1] == nums[left]:
                        left += 1
                    while right > 0 and nums[right - 1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1 
                elif curr_sum > target_sum:
                    right -= 1
                else:
                    left += 1
        
        return ret