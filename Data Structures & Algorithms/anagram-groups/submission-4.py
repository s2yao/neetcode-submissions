from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # using dict to manage tuple of letter count
        # with list to append on each group
        groupstring = defaultdict(list)

        for curr_str in strs:
            letter = [0] * 26
            for char in curr_str:
                letter[ord(char) - ord("a")] += 1
            # letter completed with curr str
            groupstring[tuple(letter)].append(curr_str)

        
        return list(groupstring.values())