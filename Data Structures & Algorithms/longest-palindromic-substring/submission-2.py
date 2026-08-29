class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""
        for i in range(len(s)):
            # Character in the middle
            j, k = i-1, i+1
            while j>=0 and k<len(s) and s[j] == s[k]:
                if(k-j+1>len(answer)): 
                    answer = s[j:k+1]
                j-=1
                k+=1

            # Characters in the middle
            j, k = i, i+1
            while j>=0 and k<len(s) and s[j] == s[k]:
                if(k-j+1>len(answer)): 
                    answer = s[j:k+1]
                j-=1
                k+=1
        if len(answer) == 0: 
            return s[0]
        return answer
        
        