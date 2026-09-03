class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)

        while count:
            curr_min = min(count)
            for _ in range(groupSize):
                if curr_min not in count:
                    return False
                if count[curr_min] == 1:
                    del count[curr_min]
                else:
                    count[curr_min] -= 1

                curr_min += 1    

        return True