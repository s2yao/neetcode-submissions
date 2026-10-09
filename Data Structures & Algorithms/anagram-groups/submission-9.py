class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def freq_arr(curr_word):
            arr = [0] * 26
            for i in range(len(curr_word)):
                curr_char = curr_word[i]
                posn = ord(curr_char) - ord('a')
                arr[posn] += 1
            return tuple(arr)
                
        map_dict = defaultdict(list)

        for word in strs:
            map_dict[freq_arr(word)].append(word)

        return [words for words in map_dict.values()]