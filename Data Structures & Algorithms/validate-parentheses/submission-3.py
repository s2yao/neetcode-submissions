class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for ele in s:
            if stack and (
                ele == "]" and stack[-1] == "[" or 
                ele == "}" and stack[-1] == "{" or 
                ele == ")" and stack[-1] == "("):
                stack.pop()
            else:
                stack.append(ele)
        
        return not stack