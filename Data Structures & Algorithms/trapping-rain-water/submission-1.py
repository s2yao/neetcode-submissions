class Solution:
    def trap(self, height: List[int]) -> int:
        # for each block: calculate ith index by min(left, right) - current height

        # left_max
        left_max = [0] * len(height)
        left_max[0] = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i])
        
        # right_max
        right_max = [0] * len(height)
        right_max[len(height) - 1] = height[len(height) - 1]
        for i in reversed(range(len(height) - 1)):
            right_max[i] = max(right_max[i + 1], height[i])

        ret = 0
        for i in range(len(height)):
            ret += min(left_max[i], right_max[i]) - height[i]

        return ret

        

        

        