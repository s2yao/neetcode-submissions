class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        curr = 0
        daNum = 0
        while True:
            if nums[curr] == 0: 
                return curr

            daNum = nums[curr]
            nums[curr] = 0
            curr = daNum
