class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ele in s:
            if stack and (
                (ele == "]" and stack[-1] == "[") 
                or (ele == "}" and stack[-1] == "{") 
                or (ele == ")" and stack[-1] == "(")
                ):
                stack.pop()
                continue
            stack.append(ele)
        
        return len(stack) == 0