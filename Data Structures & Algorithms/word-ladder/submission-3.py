class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set()

# talk
# t: 0
# a: 1
# l: 2
# k: 3

# tail
# t: 0
# a: 1
# i: 2
# l: 3

# tale



        def transform(word) -> list[str]:
            ret = []

            for target in wordList:
                if target in visited:
                    continue

                diff_char = 0
                for index in range(len(word)):
                    if word[index] != target[index]:
                        diff_char += 1

                if diff_char == 1:
                    ret.append(target)

            return ret
        
        # bfs
        def bfs(process):
            curr_step = 0

            while process:
                new_level = []
                curr_step += 1
                for word in process:
                    if word in visited:
                        continue
                    visited.add(word)
                    if word == endWord:
                        return curr_step
                    # filter all the words that i can transform
                    new_level = transform(word)
                process = new_level

            return 0
        
        return bfs([beginWord])

# beginWord="talk"
# endWord="tail"
# wordList=["talk","tons","fall","tail","gale","hall","negs"]

# lost

# most 

# mist
# {'m': 0, 'i': 1, 's': 2, 't': 3}

# miss
# {'m': 0, 'i': 1, 's': 3}