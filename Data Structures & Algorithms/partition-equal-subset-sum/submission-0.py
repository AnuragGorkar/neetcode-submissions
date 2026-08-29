class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        req_total = sum(nums)
        if req_total%2: 
            return False
        req_total//=2
        def dfs(i, sum_total):
            if i==len(nums): 
                return sum_total == req_total
            else: 
                return dfs(i+1, sum_total+nums[i]) or dfs(i+1, sum_total)
        return dfs(0, 0)

        