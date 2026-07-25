class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapper = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ret = []
        
        def get_letters(num):
            return mapper[int(num) - 2]
        
        def search(index, curr_arr):
            if index == len(digits):
                ret.append(''.join(curr_arr))
                return
            
            curr_letter = get_letters(digits[index])
            for string in curr_letter:
                search(index + 1, curr_arr + [string])

        search(0, [])
        return ret