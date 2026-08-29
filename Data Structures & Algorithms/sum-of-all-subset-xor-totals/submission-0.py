class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        def dfs(index, xor):
            nonlocal res
            if index ==len(nums):
                res += xor
            else:
                # take
                dfs(index+1, xor^nums[index])
                # not take
                dfs(index+1, xor)
        dfs(0, 0)
        return res