class Solution:
    def checkValidString(self, s: str) -> bool:
        max_left_open = 0
        min_left_open = 0

        for char in s:
            if char == '(':
                max_left_open += 1
                min_left_open += 1
            elif char == ')':
                max_left_open -= 1
                min_left_open -= 1
            else:
                max_left_open += 1
                min_left_open -= 1
            
            min_left_open = max(min_left_open, 0)
            
            if max_left_open < 0:
                return False
        
        return min_left_open == 0