class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        inc_ele = []

        def find_first_bigger_equal(num) -> int:
            if not inc_ele:
                return 0
            
            for idx, ele in enumerate(inc_ele):
                if ele >= num:
                    return idx
            
            return len(inc_ele)
        
        for ele in nums:
            idx = find_first_bigger_equal(ele)

            if idx == len(inc_ele):
                inc_ele.append(ele)
            else:
                inc_ele[idx] = ele
        
        return len(inc_ele)