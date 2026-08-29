class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [[-1]*(len(s)+1) for _ in range(len(s)+1)]
        def dfs(i, j): 
            if dp[i][j] != -1:
                return dp[i][j]
            if i==n:
                dp[i][j] = 1
                return 1 
            elif j==n:
                dp[i][j] = 1 
                return 0
            dp[i][j] = 0
            if (s[i:j+1] in wordDict and dfs(j+1, j+1)) or dfs(i, j+1):
                dp[i][j] = 1
            return dp[i][j]

        return bool(dfs(0, 0))
        