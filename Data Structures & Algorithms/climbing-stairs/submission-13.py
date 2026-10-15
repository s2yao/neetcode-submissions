class Solution:
    def climbStairs(self, n: int) -> int:
        prev1 = prev2 = 0
        curr = 1

        for _ in range(n):
            prev2 = prev1
            prev1 = curr
            curr = prev1 + prev2
            
        return curr
