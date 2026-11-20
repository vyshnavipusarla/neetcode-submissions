class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        l=len(hand)
        if l%groupSize!=0:
            return False
        count=Counter(hand)
        for num in hand:
            if count[num]:
                for i in range(num,num+groupSize):
                    if not count[i]:
                        return False
                    count[i]-=1
        return True

        