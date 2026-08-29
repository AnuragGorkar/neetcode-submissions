class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [[-sys.maxsize]*(len(nums)+1) for _ in range(len(nums)+1)]
        ans = -sys.maxsize
        def dfs(i, j):
            nonlocal ans
            if dp[i][j] != -sys.maxsize: 
                return dp[i][j]
            elif i==j: 
                dp[i][j] = nums[i]
                ans = max(ans, nums[i])
            else:
                res1 = dfs(i+1, j) 
                res2 = dfs(i, j-1) 
                res3 = -sys.maxsize
                if j-i>=2: 
                    res3 = dfs(i+1, j-1)
                ans = max(ans, res1, res2, res3, nums[i]*res1)
                dp[i][j] = nums[i]*res1
            return dp[i][j]

        dfs(0, len(nums)-1)
        return ans   