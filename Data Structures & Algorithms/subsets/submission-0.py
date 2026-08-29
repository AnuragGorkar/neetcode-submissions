class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums, index, curr_res):
            if index == len(nums): 
                res.append(curr_res[:])
            else: 
                dfs(nums, index+1, curr_res)
                curr_res.append(nums[index])
                dfs(nums, index+1, curr_res)
                curr_res.pop()
        curr_res = [] 
        dfs(nums, 0, curr_res)
        return res 
            

        