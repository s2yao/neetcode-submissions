class Solution:
    def reverseBits(self, n: int) -> int:
        ret = 0
        for i in range(32):
            mask = 1 & n
            ret <<= 1
            ret |= mask
            n >>= 1
        return ret