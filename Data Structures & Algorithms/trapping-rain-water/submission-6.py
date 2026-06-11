class Solution:
    def trap(self, height: List[int]) -> int:
        # 2 ptr
        # ret adds current - last
        # keep track of current max on both side, to know if current element can be filled
        # Excluding both side
        ret = 0
        left = 0
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]

        while left < right:
            if max_left < max_right:
                left += 1
                # max of left must > current ele
                if height[left] < max_left:
                    ret += max_left - height[left]
                else:
                    max_left = height[left]
            else:
                right -= 1
                if height[right] < max_right:
                    ret += max_right - height[right]
                else:
                    max_right = height[right]
        
        return ret

