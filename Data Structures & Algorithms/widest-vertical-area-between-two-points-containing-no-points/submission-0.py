class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        ret = 0
        for i in range(1, len(points)):
            ret = max(ret, points[i][0] - points[i - 1][0])
        
        return ret