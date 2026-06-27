class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        fuck = [0] * 26

        # seed
        for ele in s:
            fuck[ord(ele) - ord('a')] += 1
        
        for ele in t:
            fuck[ord(ele) - ord('a')] -= 1

        for idx in fuck:
            if idx != 0:
                return False
        
        return True
        
