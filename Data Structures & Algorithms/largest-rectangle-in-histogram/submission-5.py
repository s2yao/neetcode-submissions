class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ret = 0
        for idx, height in enumerate(heights):
            new_idx = idx
            while stack and stack[-1][1] > height:
                curr_idx, curr_height = stack.pop()
                width = idx - curr_idx
                curr_area = curr_height * width
                ret = max(ret, curr_area)
                new_idx = curr_idx
            stack.append([new_idx, height])

        print(stack)
        if stack:
            while stack:
                curr_idx, curr_height = stack.pop()
                width = len(heights) - curr_idx
                curr_area = curr_height * width
                ret = max(ret, curr_area)
        
        return ret