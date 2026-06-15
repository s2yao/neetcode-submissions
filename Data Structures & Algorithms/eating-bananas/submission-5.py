class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search
        right = max(piles)
        left = 1
        ret = 0

        # binary search towards every possible potential ret
        while left <= right:
            mid = (left + right) // 2
            curr_hour = 0
            # curr hour it takes for mid as speed
            for banana in piles:
                # ceil(banana / mid)
                curr_hour += (banana + mid - 1) // mid
            
            if curr_hour <= h:
                # record potential ret
                ret = mid
                # but look for slower speed
                right = mid - 1
            else:
                # not fast enough
                left = mid + 1
        
        return ret

