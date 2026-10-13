class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        mapper_onebased = ['','',"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        
        curr = []
        ret = []

        def backtrack(idx):
            if idx == len(digits):
                ret.append("".join(curr))
                return

            curr_digit = int(digits[idx])
            print(curr_digit)
            for char in mapper_onebased[curr_digit]:
                curr.append(char)
                backtrack(idx + 1)
                curr.pop()


        backtrack(0)
        return ret