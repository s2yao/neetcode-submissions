class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        queue = deque([0])
        dict_set = set(wordDict)
        visited = set()

        def match(start_idx):
            ret = []
            idx = start_idx
            while idx < (len(s) + 1):
                curr_word = s[start_idx:idx]
                if curr_word in dict_set and idx not in visited:
                    ret.append(idx)
                    visited.add(idx)
                idx += 1
            return ret
        
        while queue:
            next_lvl = len(queue)
            for i in range(next_lvl):
                curr_idx = queue.popleft()
                print(curr_idx)
                if curr_idx == len(s):
                    return True
                queue.extend(match(curr_idx))
        
        return False

