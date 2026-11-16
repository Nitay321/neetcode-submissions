class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        counts = collections.Counter(hand)

        for card in sorted(counts):
            while counts[card] > 0:
                for i in range(card,card+groupSize):
                    if counts[i] == 0:
                        return False
                    counts[i] -= 1
        return True










