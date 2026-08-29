class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1] * (n+1)
        def dfs(i):
            if dp[i] != -1: 
                return dp[i]
            if i==n: 
                dp[i] = 1
            elif s[i]=='0': 
                dp[i] = 0
            else: 
                res = dfs(i+1)
                if i<n-1 and ((s[i] == '1' and s[i+1] in '1234567890') or (s[i] =='2' and s[i+1] in '1234560')):
                    res += dfs(i+2)
                dp[i] = res
            return dp[i]

        return dfs(0)
        
        