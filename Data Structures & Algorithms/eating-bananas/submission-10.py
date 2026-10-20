class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ret = right

        def can_finish(speed):
            hours = 0
            for pile in piles:
                hours += (pile + speed - 1) // speed
            return hours
        
        while left <= right:
            mid = (left + right) // 2

            time = can_finish(mid)


            if time > h:
                left = mid + 1
            else:
                right = mid - 1
                ret = min(ret, mid)
        
        return ret