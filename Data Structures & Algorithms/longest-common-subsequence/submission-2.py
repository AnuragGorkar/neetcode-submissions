class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1) 
        n = len(text2)
        prev_dp = [0] * n
        if text1[0] == text2[0]:
            prev_dp[0] = 1 
        for j in range(1, n): 
            if text1[0] == text2[j]: 
                prev_dp[j] = 1
            else: 
                prev_dp[j] = prev_dp[j-1]
        dp = [0] * n
        for i in range(1, m): 
            if text1[i] == text2[0]: 
                dp[0] = 1
            else: 
                dp[0] = prev_dp[0]
            for j in range(1, n): 
                if text1[i] == text2[j]: 
                    dp[j] = prev_dp[j-1] + 1
                else: 
                    dp[j] = max(prev_dp[j], dp[j-1])
            prev_dp = dp.copy()
        return prev_dp[n-1]