class Solution:
    def climbStairs(self, n: int) -> int:
        step_1 = 1
        step_2 = 0

        for _ in range(n):
            curr = step_1 + step_2
            step_2 = step_1
            step_1 = curr

        return step_1
