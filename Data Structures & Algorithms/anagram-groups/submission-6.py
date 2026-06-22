class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # make a unique 26 len comb for each
        # store into a dict

        dict_category = defaultdict(list)

        for ele in strs:
            curr = [0] * 26
            for char in ele:
                curr[ord(char) - ord('a')] += 1
            dict_category[tuple(curr)].append(ele)
        
        ret = []
        for categories in dict_category.values():
            ret.append(categories)
        
        return ret