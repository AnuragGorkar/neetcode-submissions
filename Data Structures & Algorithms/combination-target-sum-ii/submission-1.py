class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(index, curr_res, curr_sum):
            if index == len(nums):
                if curr_sum == target: 
                    res.append(curr_res[:])
                return
            if curr_sum>target: 
                return
            curr_res.append(nums[index])
            dfs(index+1, curr_res, curr_sum+nums[index])
            curr_res.pop()
            index += 1
            while index<len(nums) and nums[index] == nums[index-1]: 
                index += 1
            dfs(index, curr_res, curr_sum)
        dfs(0, [], 0)
        return res
        