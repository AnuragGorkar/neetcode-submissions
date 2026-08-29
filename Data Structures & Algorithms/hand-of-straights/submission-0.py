class Solution:
    def isNStraightHand(self, hand: List[int], group_size: int) -> bool:
        if len(hand)%group_size:
            return False
        hand.sort()
        group_count = 0

        while True:
            curr_size, prev_hand = 0, None
            for i in range(len(hand)):
                if hand[i] != -1 and ((prev_hand == None) or hand[i] == (prev_hand+1)):
                    curr_size += 1
                    prev_hand = hand[i]
                    hand[i] = -1
                    if curr_size == group_size:
                        group_count += 1
                        break
            if curr_size != group_size:
                break
 
        return group_count == (len(hand)/group_size)