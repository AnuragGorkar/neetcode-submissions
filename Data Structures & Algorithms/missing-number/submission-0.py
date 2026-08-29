class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res1, res2 = 0, 0
        for index, num in enumerate(nums): 
            res1 ^= num
            res2 ^= index
        res2 ^= len(nums)
        return res1 ^ res2
        