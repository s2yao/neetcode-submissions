class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # count sort
        curr_posn = 0
        record = nums[0]
        while True:
            if nums[curr_posn] == 0:
                return record
            # record down current
            record = nums[curr_posn]
            # make it 0
            nums[curr_posn] = 0
            # jump
            curr_posn = record
        