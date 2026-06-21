class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # use floyd fast slow pointer
        fast = 0
        slow = 0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if fast == slow:
                break

        slow2 = 0
        while slow2 != slow:
            slow2 = nums[slow2]
            slow = nums[slow]
        
        return slow