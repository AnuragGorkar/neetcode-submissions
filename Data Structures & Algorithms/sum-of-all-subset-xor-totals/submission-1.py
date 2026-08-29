class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(index, xor):
            if index ==len(nums):
                return xor
            else:
                return dfs(index+1, xor^nums[index]) + dfs(index+1, xor)                
        return dfs(0, 0)