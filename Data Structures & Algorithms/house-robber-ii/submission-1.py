class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def calculate(new_houses):
            acc1 = 0
            acc2 = 0

            for house in new_houses:
                curr = max(house + acc2, acc1)
                acc2 = acc1
                acc1 = curr
            
            return acc1
        
        return max(calculate(nums[1:]), calculate(nums[:-1]))