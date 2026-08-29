class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dfs(i, prev):
            if i==len(nums): 
                return 0
            else: 
                not_take = dfs(i+1, prev)
                take = -sys.maxsize
                if(nums[i]>prev): 
                    take = 1+dfs(i+1, nums[i])
                return max(take, not_take)
        
        return dfs(0, -sys.maxsize)
