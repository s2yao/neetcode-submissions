from collections import Counter

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ret = 0
        
        for num in num_set:
            if num - 1 in num_set:
                continue
            
            curr_max = 0
            curr_num = num
            while curr_num in num_set:
                curr_max += 1
                curr_num += 1
            
            ret = max(ret, curr_max)
        
        return ret