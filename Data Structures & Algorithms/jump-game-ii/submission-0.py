class Solution:
    def jump(self, nums: List[int]) -> int:
        res = [1e9] * len(nums)
        res[0] = 0
        for i in range(len(nums)):
            for j in range(min(i+nums[i], len(nums)-1), i, -1):
                res[j] = min(res[j], res[i]+1)
        return res[len(nums)-1]
        