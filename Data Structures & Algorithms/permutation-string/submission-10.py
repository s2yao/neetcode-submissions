class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)
        while r <= len(s2):
            if Counter(s1) == Counter(s2[l:r]):
                return True
            r += 1
            l += 1
        return False