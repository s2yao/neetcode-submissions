class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        curr_idx = 0
        while True:
            curr_num = nums[curr_idx]

            if curr_num == -1:
                return curr_idx
            
            nums[curr_idx] = -1
            curr_idx = curr_num
        
        # idx = 0
        # num = 1

        # idx = 1
        # num = 2

        # idx = 2
        # num = 3

        # idx = 3
        # num = 2

        # idx = 2
        # num = -1