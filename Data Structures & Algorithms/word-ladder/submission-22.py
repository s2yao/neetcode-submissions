class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        queue = deque([beginWord])
        ret = 0
        visited = set([beginWord])
        while queue:
            curr_len = len(queue)
            ret += 1
            for _ in range(curr_len):
                curr_word = queue.popleft()
                if curr_word == endWord:
                    return ret
                for i in range(len(curr_word)):
                    for char in "qwrtyuiopasdfghjklzxcvbnme":
                        new_word = curr_word[:i] + char + curr_word[i+1:]
                        if new_word not in word_set:
                            continue
                        if new_word in visited:
                            continue
                        
                        queue.append(new_word)
                        visited.add(new_word)
        
        return 0