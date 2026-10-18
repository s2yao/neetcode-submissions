class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        dep = defaultdict(set)
        for word in words:
            for char in word:
                dep[char]
        for i in range(1, len(words)):
            curr_word = words[i]
            prev_word = words[i-1]

            if len(prev_word) > len(curr_word) and prev_word.startswith(curr_word):
                return ""
            idx = 0
            while idx < len(curr_word) and idx < len(prev_word):
                curr_word_char = curr_word[idx]
                prev_word_char = prev_word[idx]
                if curr_word_char != prev_word_char:
                    dep[prev_word_char].add(curr_word_char)
                    break

                idx += 1

        visited = set()
        curr_path = set()
        ret = []

        def dfs(char):
            if char in curr_path:
                return False
            if char in visited:
                return True
            
            visited.add(char)
            curr_path.add(char)
            for next_char in dep[char]:
                if not dfs(next_char):
                    return False
            curr_path.discard(char)
            ret.append(char)
            return True
        
        for char in dep:
            if not dfs(char):
                return ""
        
        ret = ret[::-1]
        print(ret, "hi")
        return "".join(ret)