class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): 
            return False

        # 2 pointer solution
        s1_count = [0] * 26
        s2_count = [0] * 26

        # initial seeding
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        match = 0

        # scan for initial matches
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                match += 1
        
        if match == 26: 
            return True
        
        l = 0
        # the window
        for r in range(len(s1), len(s2)):
            # adding right
            idx_add = ord(s2[r]) - ord('a')

            # check if previous match
            if s2_count[idx_add] == s1_count[idx_add]:
                match -= 1

            # shove into count2
            s2_count[idx_add] += 1
            if s2_count[idx_add] == s1_count[idx_add]:
                match += 1
            


            # adding right
            idx_remove = ord(s2[l]) - ord('a')

            # check if previous match
            if s2_count[idx_remove] == s1_count[idx_remove]:
                match -= 1

            # shove into s2
            s2_count[idx_remove] -= 1
            if s2_count[idx_remove] == s1_count[idx_remove]:
                match += 1
            l += 1


            if match == 26:
                return True
        # no match
        return False



