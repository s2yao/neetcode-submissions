class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()

        for idx, ele in enumerate(nums):
            if idx > 0 and ele == nums[idx - 1]:
                continue
            
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                val = ele + nums[left] + nums[right]
                if val == 0:
                    ret.append([ele, nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                    
                elif val > 0:
                    right -= 1
                else:
                    left += 1
            
        
        return ret