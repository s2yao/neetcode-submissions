class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we use dictionary to store:
        # 1: a tuple of 26 letters
        # 2: a list containing the result, matching each tuple
        strlst_tuple_dict = defaultdict(list)

        for word in strs:
            letters = [0] * 26
            for char in word:
                letters[ord(char) - ord('a')] += 1
            
            strlst_tuple_dict[tuple(letters)].append(word)
        
        return list(strlst_tuple_dict.values())
