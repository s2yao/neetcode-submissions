class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        letter = [0] * 26

        for i in range(len(s)):
            letter[ord(s[i]) - ord('a')] += 1
        
        for i in range(len(t)):
            letter[ord(t[i]) - ord('a')] -= 1

        for ele in letter:
            if ele != 0: return False
        
        return True