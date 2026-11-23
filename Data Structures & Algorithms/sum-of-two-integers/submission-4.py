class Solution:
    def getSum(self, a: int, b: int) -> int:
        a &= 0xFFFFFFFF
        b &= 0xFFFFFFFF
        bit_limit = 0x7FFFFFFF

        while b:
            temp_xor = a ^ b
            temp_and = (a & b) << 1
            a = temp_xor
            b = temp_and & 0xFFFFFFFF
        
        if a <= bit_limit:
            return a
        return ~(a ^ 0xFFFFFFFF)