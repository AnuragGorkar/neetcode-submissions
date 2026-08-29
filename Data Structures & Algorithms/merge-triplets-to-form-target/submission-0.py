class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        count = 0
        first, second, third = False, False, False
        for triplet in triplets:
            if triplet[0]==target[0] and triplet[1]<=target[1] and triplet[2]<=target[2]:
                first = True
            if triplet[0]<=target[0] and triplet[1]==target[1] and triplet[2]<=target[2]:
                second = True
            if triplet[0]<=target[0] and triplet[1]<=target[1] and triplet[2]==target[2]:
                third = True
            if first and second and third:
                return True
        return first and second and third