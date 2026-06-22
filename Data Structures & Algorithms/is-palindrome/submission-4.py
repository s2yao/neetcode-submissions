class Solution:
    def isPalindrome(self, s: str) -> bool:
        ptr1 = 0
        ptr2 = len(s) - 1

        while ptr1 < ptr2:
            if not s[ptr1].isalnum():
                ptr1 += 1
                continue
            elif not s[ptr2].isalnum():
                ptr2 -= 1
                continue
            
            if s[ptr1].lower() != s[ptr2].lower():
                return False
            
            ptr1 += 1
            ptr2 -= 1
        
        return True