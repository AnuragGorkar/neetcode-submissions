class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(index, curr_res, curr_sum):
            if index == len(nums):
                if curr_sum == target: 
                    res.append(curr_res[:])
                return
            if curr_sum>target: 
                return
            curr_res.append(nums[index])
            dfs(index, curr_res, curr_sum+nums[index])
            curr_res.pop()
            dfs(index+1, curr_res, curr_sum)
        dfs(0, [], 0)
        return res
