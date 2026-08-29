class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        n = len(coins)
        dp = [[-1] * (amount+1) for _ in range(n+1)]

        def dfs(i, amount): 
            print(i, amount)
            if dp[i][amount] != -1: 
                return dp[i][amount]
            if amount==0: 
                res = 0
            elif i==n: 
                res = sys.maxsize
            else: 
                res = dfs(i+1, amount)
                if amount>=coins[i]:
                    res  = min(res, dfs(i, amount-coins[i])+1)
            dp[i][amount] = res
            return res
        
        ans = dfs(0, amount)
        if ans == sys.maxsize:
            return -1
        return ans
        