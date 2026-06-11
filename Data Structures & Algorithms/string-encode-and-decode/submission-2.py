class Solution:

    def encode(self, strs: List[str]) -> str:
        # putting the length of current string and # at the beginning
        ret = ""

        for ele in strs:
            ret += str(len(ele)) + "#" + ele
        
        return ret

    def decode(self, s: str) -> List[str]:
        # im given a string with length, delimiter, and actual content
        ret = []

        i = 0
        while i < len(s):
            right_length = i
            
            while s[right_length] != "#":
                right_length += 1
            
            # ATP, right_length should sit directly on #
            length = int(s[i:right_length])

            ret.append(s[right_length + 1: right_length + 1 + length])
            i = right_length + 1 + length

        return ret