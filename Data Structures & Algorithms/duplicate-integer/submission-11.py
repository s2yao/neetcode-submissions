class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        curr_set = set()

        for ele in nums:
            if ele not in curr_set:
                curr_set.add(ele)
            else: # ele in the current set
                return True
        
        return False
