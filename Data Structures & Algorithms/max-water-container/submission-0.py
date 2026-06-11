class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ptr1 = 0
        ptr2 = len(heights) - 1

        ret = 0
        curr_max = 0

        while ptr1 < ptr2:
            curr_max = min(heights[ptr1], heights[ptr2]) * (ptr2 - ptr1)
            ret = max(ret, curr_max)

            if heights[ptr1] == heights[ptr2]:
                ptr1 += 1
                ptr2 -= 1
            elif heights[ptr1] < heights[ptr2]: # 1 smaller
                ptr1 += 1
            else:
                ptr2 -= 1
        
        return ret