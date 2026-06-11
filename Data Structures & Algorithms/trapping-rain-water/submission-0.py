class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total_water = 0

        for i in range(n):
            # Find the tallest bar to the left of i (including i)
            max_left = max(height[:i + 1])

            # Find the tallest bar to the right of i (including i)
            max_right = max(height[i:])

            # Water trapped at position i
            trapped = min(max_left, max_right) - height[i]
            total_water += trapped

        return total_water
