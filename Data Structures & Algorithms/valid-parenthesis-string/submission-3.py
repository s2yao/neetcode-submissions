class Solution:
    def checkValidString(self, s: str) -> bool:
        stack_idx = []
        asterisk_idx = [False] * len(s) 

        def find_asterisk(start, end):
            for idx in reversed(range(start, end)):
                if asterisk_idx[idx] == True:
                    asterisk_idx[idx] = False
                    return True
            return False
                
        for idx in range(len(s)):
            if s[idx] == "*":
                asterisk_idx[idx] = True
            elif s[idx] == ")":
                if not stack_idx:
                    if not find_asterisk(0, idx):
                        return False
                elif s[stack_idx[-1]] != "(":
                    if not find_asterisk(stack_idx[-1], idx):
                        return False
                # there is corresponding
                else:
                    stack_idx.pop()
            else:
                stack_idx.append(idx)
        
        while stack_idx:
            open_idx = stack_idx.pop()

            if not find_asterisk(open_idx + 1, len(s)):
                return False

        return True