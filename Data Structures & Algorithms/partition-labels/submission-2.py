class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ret_arr = []
        left = 0
        last_posn = defaultdict(int)
        # find last appearing position for each char
        for idx, char in enumerate(s):
            last_posn[char] = idx

        need_to_travel = 0

        # "right" iteration of s:
        for right in range(len(s)):
            # right > need_to_travel:
            if right > need_to_travel:
                # record current window into ret_arr
                ret_arr.append(right - left)
                # left update
                left = right
            
            # update need_to_travel on new further distance
            need_to_travel = max(need_to_travel, last_posn[s[right]])
        
        ret_arr.append(len(s) - left)
        
        return ret_arr