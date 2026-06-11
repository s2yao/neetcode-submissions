class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ret = 0
        mono_stack = []

        for idx, val in enumerate(heights):
            curr_idx = idx
            while mono_stack and mono_stack[-1][1] >= val:
                elim_idx, elim_val = mono_stack.pop()
                ret = max(ret, (idx - elim_idx) * elim_val)
                curr_idx = elim_idx
            mono_stack.append((curr_idx, val))
        
        # data clean - horizontal
        for ele in mono_stack:
            ret = max(ret, (len(heights) - ele[0]) * ele[1])
        
        return ret
