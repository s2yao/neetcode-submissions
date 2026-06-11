class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ret = 0

        # inc. mono stack to elinminate element bigger than current element
        # (curr_idx, bar_height)
        stack = []

        for i in range(len(heights)):
            curr_idx = i
            while stack and stack[-1][1] > heights[i]:
                idx, height = stack.pop()
                ret = max(ret, height * (i - idx))
                curr_idx = idx
            stack.append((curr_idx, heights[i]))
            
        for ele in stack:
            ret = max(ret, ele[1] * (len(heights) - ele[0]))
        return ret