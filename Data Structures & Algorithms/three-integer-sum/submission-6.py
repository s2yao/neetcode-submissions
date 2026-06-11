class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 2 ptr

        nums.sort()
        
        ret = []

        for i in range(len(nums)):
            print(nums)
            print("i:", i)

            # optimization
            if nums[i] > 0:
                break

            # skipping dup
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # left right ptr
            left_j = i + 1
            right_k = len(nums) - 1

            while left_j < right_k:
                print("left_j", left_j)
                print("right_k", right_k)
                ans = nums[i] + nums[left_j] + nums[right_k]

                if ans < 0: # need increase
                    left_j += 1
                elif ans > 0: # need decrease
                    right_k -= 1
                else:
                    ret.append([nums[i], nums[left_j], nums[right_k]])
                    left_j += 1
                    right_k -= 1

                    while left_j < right_k and nums[left_j] == nums[left_j - 1]:
                        left_j += 1

                
        return ret
