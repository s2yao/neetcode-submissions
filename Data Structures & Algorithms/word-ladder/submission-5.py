class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set()

        # to check for diff chars from curr word to all the word in wordList
        def check(word):
            ret = []

            for target_word in wordList:
                if target_word in visited:
                    continue
                count = 0
                for index in range(len(word)):
                    if word[index] != target_word[index]:
                        count += 1
                if count == 1:
                    ret.append(target_word)
            return ret

        # multi point bfs
        def bfs(process):
            curr_step = 0

            while process:
                next_lvl = []
                curr_step += 1
                for curr_word in process:
                    if curr_word in visited:
                        continue
                    visited.add(curr_word)
                    if curr_word == endWord:
                        return curr_step
                    next_lvl = check(curr_word)
                process = next_lvl
            
            return 0
        return bfs([beginWord])

# beginWord = "cat", endWord = "sag", wordList = ["bat","bag","sag","dag","dot"]
# visited = cat
# process = [cat]
# next_lvl = [bat]
# curr_step = 1

# process = [cat]
# next_lvl = [bat]
# curr_step = 1

# a
