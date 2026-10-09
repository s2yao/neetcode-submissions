class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ret = right

        def can_finish(speed):
            ret = 0
            for pile in piles:
                ret += (pile + speed - 1) // speed
            return ret

        while left <= right:
            eat_speed_mid = (left + right) // 2
            if can_finish(eat_speed_mid) <= h:
                ret = min(ret, eat_speed_mid)
                right = eat_speed_mid - 1
            else:
                left = eat_speed_mid + 1

        return ret