class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0

        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ")":
                low -= 1
                high -= 1
            else:
                high += 1 # choosing "("
                low -= 1 
            
            if high < 0:
                return False
            # num of ) <= nums of * + (
            if low < 0: # * == ""
                low = 0
        
        return low == 0