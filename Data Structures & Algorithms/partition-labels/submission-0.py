class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = defaultdict(int)

        for i, c in enumerate(s):
            lastIndex[c] = i

        ret = []
        end = size = 0

        for i, c in enumerate(s):
            size += 1
            end = max(end, lastIndex[c])

            if i == end:
                ret.append(size)
                size = 0

        return ret
