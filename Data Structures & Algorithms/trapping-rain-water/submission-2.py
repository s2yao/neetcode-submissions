class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        # 2 pointer
        # let left, right pointer record the current max
        # always look for a lower wall to update, safe to update

        l = 0
        r = len(height) - 1
        left_max = height[l]
        right_max = height[r]
        ret = 0

        while l < r:
            # if one side had lower wall, we move that side ptr inward
            # look for potentially higher wall
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                # if the new position is lower than the height that we have saw
                ret += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                ret += right_max - height[r]
            
        return ret





