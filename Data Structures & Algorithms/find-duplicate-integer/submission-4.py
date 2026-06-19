class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # # count sort
        # curr_posn = 0
        # record = nums[0]
        # while True:
        #     if nums[curr_posn] == 0:
        #         return record
        #     # record down current
        #     record = nums[curr_posn]
        #     # make it 0
        #     nums[curr_posn] = 0
        #     # jump
        #     curr_posn = record
        

        # fast and slow pointer
        fast = 0
        slow = 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if fast == slow:
                break

        # ATP fast/slow pointer at a cycle
        slow1 = 0
        while True:

            slow1 = nums[slow1]
            slow = nums[slow]
            
            if slow == slow1:
                return slow