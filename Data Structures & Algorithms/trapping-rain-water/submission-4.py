class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        ret = 0

        while left < right:
            if left_max < right_max:
                left += 1
                # water trapped at 'left' is bounded by left_max (since right side is taller)
                if height[left] < left_max:
                    ret += left_max - height[left]
                left_max = max(left_max, height[left])
            else:
                right -= 1
                # water trapped at 'right' is bounded by right_max (since left side is taller/equal)
                if height[right] < right_max:
                    ret += right_max - height[right]
                right_max = max(right_max, height[right])


        return ret
