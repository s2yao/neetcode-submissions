class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we get the max of arrary
        # try to find the value that fits
        left = 1
        right = max(piles)
        ret = right

        while left <= right:
            # calculate current hour taken
            hour_taken = 0
            mid = (left + right) // 2
            for banana in piles:
                curr = 0
                hour_taken += (banana + mid - 1) // mid

            if hour_taken <= h:
                ret = mid
                # this speed works, but how about slower?
                right = mid - 1
            else:
                # need speed
                left = mid + 1
            
        return ret

