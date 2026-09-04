class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for ele in sorted(hand):
            while count[ele] > 0:
                curr = ele
                for _ in range(groupSize):
                    if curr not in count:
                        return False
                    count[curr] -= 1
                    curr += 1
        
        return True