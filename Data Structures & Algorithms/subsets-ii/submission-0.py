class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(nums, index, curr_res):
            if index == len(nums): 
                res.append(curr_res[:])
            else:
                curr_res.append(nums[index])
                dfs(nums, index+1, curr_res)
                curr_res.pop()
                index += 1
                while index<len(nums) and nums[index] == nums[index-1]: 
                    index+=1
                dfs(nums, index, curr_res)
        dfs(nums, 0, [])       
        return res
        