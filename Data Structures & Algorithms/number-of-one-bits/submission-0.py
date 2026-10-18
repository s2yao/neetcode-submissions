class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            curr_comp = 1 << i
            if curr_comp & n:
                res += 1
        
        return res