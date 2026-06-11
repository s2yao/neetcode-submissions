class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        # 2 ptrs
        left = 0 
        right = len(height) - 1
        # the idea is to record down the max_left and max_right
        max_left = height[left]
        max_right = height[right]
        ret = 0

        while left < right:
            if max_left < max_right:
                # left to update
                left += 1
                if max_left > height[left]:
                    ret += max_left - height[left]
                else:
                    max_left = height[left]
            else:
                # right to update
                right -= 1
                if max_right > height[right]:
                    ret += max_right - height[right]
                else:
                    max_right = height[right]
        

        return ret

