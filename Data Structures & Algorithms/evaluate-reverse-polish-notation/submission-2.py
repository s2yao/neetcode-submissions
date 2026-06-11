class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        curr_operator = ""
        result = []
        
        for curr_notation in range(len(tokens)): # O(n)
            if tokens[curr_notation] == "+":
                right = result.pop()
                left = result.pop()
                result.append(left + right)
            elif tokens[curr_notation] == "-":
                right = result.pop()
                left = result.pop()
                result.append(left - right)
            elif tokens[curr_notation] == "*":
                right = result.pop()
                left = result.pop()
                result.append(left * right)
            elif tokens[curr_notation] == "/":
                right = result.pop()
                left = result.pop()
                result.append(int(left / right))
            else:
                result.append(int(tokens[curr_notation]))
            print(result)
        
        return result[0]

