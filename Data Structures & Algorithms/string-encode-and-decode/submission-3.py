class Solution:

    def encode(self, strs: List[str]) -> str:
        # putting the length of current string and # at the beginning
        ret = ""

        for ele in strs:
            ret += str(len(ele)) + "#" + ele
        
        return ret

    def decode(self, s: str) -> List[str]:
        # im given a string with length, delimiter, and actual content
        i = 0
        ret = []

        while i < len(s):
            curr_length = i

            while s[curr_length] != '#':
                curr_length += 1

            # ATP, curr_length should sit directly on #
            length = int(s[i:curr_length])

            ret.append(s[curr_length + 1: curr_length + 1 + length])

            # proceeding with next word
            i = curr_length + 1 + length
        
        return ret