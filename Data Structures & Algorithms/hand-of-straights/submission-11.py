from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)

        for card in hand:
            if not count[card]:
                continue
            curr = card
            while count[curr - 1]:
                curr -= 1
            
            while curr <= card:
                while count[curr]:
                    for i in range(curr, curr + groupSize):
                        if not count[i]:
                            return False
                        count[i] -= 1
                curr += 1

        return True