from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        inc_ele = []
        
        for ele in nums:
            idx = bisect_left(inc_ele, ele)

            if idx == len(inc_ele):
                inc_ele.append(ele)
            else:
                inc_ele[idx] = ele
        
        return len(inc_ele)