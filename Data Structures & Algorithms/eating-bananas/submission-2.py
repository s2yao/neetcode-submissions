class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ret = right

        while left <= right:
            mid = (left + right) // 2
            hour_taken = 0

            for banana in piles:
                hour_taken += (banana + mid - 1) // mid

            if hour_taken <= h:
                ret = mid
                right = mid - 1
            else:
                left = mid + 1

        return ret