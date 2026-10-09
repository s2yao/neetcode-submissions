from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []

        # loop through eveyr elemetn
        # look on the right for negative number
        # look for possible combination with 2 ptrs, O(n^2)
        for i, val in enumerate(nums):
            # skip dups
            # look on right to process at least one with the current duplicating element
            if i > 0 and val == nums[i - 1]:
                continue

            # if val > 0 since sorted
            # the rest is positive
            if val > 0:
                break

            leftptr = i + 1
            rightptr = len(nums) - 1

            while leftptr < rightptr:
                curr_val = val + nums[leftptr] + nums[rightptr]
                if curr_val == 0:
                    ret.append([val, nums[leftptr], nums[rightptr]])
                    rightptr -= 1
                    leftptr += 1
                    # duplicate handling for left/right ptr
                    # left
                    while (leftptr < rightptr) and nums[leftptr] == nums[leftptr - 1]:
                        leftptr += 1
                    # right
                    while (leftptr < rightptr) and nums[rightptr] == nums[rightptr + 1]:
                        rightptr -= 1

                elif curr_val > 0: # dec
                    rightptr -= 1
                else:
                    leftptr += 1 

        return ret

