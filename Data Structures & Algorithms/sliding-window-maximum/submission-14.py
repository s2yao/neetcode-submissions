class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # decreasing monotonic deque of indices
        mono = deque()
        ret = []

        for right in range(len(nums)):
            # remove smaller values from the back
            while mono and nums[mono[-1]] < nums[right]:
                mono.pop()

            mono.append(right)

            # left boundary of current window
            window_left = right - k + 1

            # remove index outside current window
            if mono[0] < window_left:
                mono.popleft()

            # append max once window size reaches k
            if right >= k - 1:
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
