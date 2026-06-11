class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # dp
        left = [0] * len(nums)
        right = [0] * len(nums)
        curr_left = nums[0]
        curr_right = nums[-1]

        # seeding the left and right
        for i in range(len(nums)):
            # left
            if i % k == 0:
                curr_left = nums[i]
            else:
                curr_left = max(curr_left, nums[i])
            left[i] = curr_left
            
            # right
            if (len(nums) - i - 1) % k == 0:
                curr_right = nums[len(nums) - i - 1]
            else:
                curr_right = max(curr_right, nums[len(nums) - i - 1])
            right[len(nums) - i - 1] = curr_right

        
        print(left, right)

        # construct return
        ret = []
        for i in range(len(nums) - k + 1):
            ret.append(max(left[i + k - 1], right[i]))
        
        return ret