from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # using a dictionary to manage the tuple
        str_tuple_dict = defaultdict(list) # dict{(tuple) : []str}

        for curr_str in strs:
            letter = [0] * 26
            # collect the letter count
            for char in curr_str:
                letter[ord(char) - ord('a')] += 1
            
            # we have the letter count
            # store to str_tuple_dict
            str_tuple_dict[tuple(letter)].append(curr_str)
        
        return list(str_tuple_dict.values()) # return the list containing all values