class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        mono_stack = []
        ret = 0
        
        for idx, height in enumerate(heights):
            new_idx = idx
            new_height = height
            while mono_stack and mono_stack[-1][1] > height:
                curr_idx, curr_height = mono_stack.pop()
                width = idx - curr_idx
                area = width * curr_height
                ret = max(ret, area)
                new_idx = curr_idx
            mono_stack.append([new_idx, new_height])


        while mono_stack:
            curr_idx, curr_height = mono_stack.pop()
            width = len(heights) - curr_idx
            area = width * curr_height
            ret = max(ret, area)
        
        return ret