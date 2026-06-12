class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # inc monotonic deque
        mono = deque()
        ret = []

        # seed the window
        for i in range(k):
            while mono and nums[mono[-1]] < nums[i]:
                mono.pop()
            mono.append(i)

        ret.append(nums[mono[0]])
        
        for window_left in range(1, len(nums) - k + 1):
            if mono and mono[0] < window_left:
                mono.popleft()
            while mono and nums[mono[-1]] < nums[window_left + k - 1]:
                mono.pop()
            mono.append(window_left + k - 1)
            ret.append(nums[mono[0]])
        
        return ret



        # # dp to store prefixes from both side, up to cutpoints
        # ret = []
        # # left dp
        # leftdp = []
        # rightdp = []
        # curr_left = 0
        # curr_right = 0

        # # seed the dp
        # for i in range(len(nums)):
        #     # seed leftdp
        #     if i % k == 0:
        #         curr_left = nums[i]
        #     else:
        #         curr_left = max(nums[i], curr_left)
        #     leftdp.append(curr_left)

        #     # seed rightdp
        #     if (len(nums) - i - 1) % k == 0:
        #         curr_right = nums[(len(nums) - i - 1)]
        #     else:
        #         curr_right = max(nums[(len(nums) - i - 1)], curr_right)
        #     rightdp.append(curr_right)
        

        # # constructing ret
        # # loop through all windows
        # for window in range(len(nums) - k + 1):
        #     ret.append(max(leftdp[window + k - 1], rightdp[len(nums) - window - 1]))
        
        # return ret
