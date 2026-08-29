class Solution:
    def isPalindrome(self, s, i, j): 
        if i>j: 
            return False
        else: 
            while i<j: 
                if not s[i] == s[j]: 
                    return False
                i+=1
                j-=1
            return True
            
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []
        pal = [[False]*len(s) for _ in range(len(s))]

        for i in range(len(s)-1, -1, -1): 
            for j in range(i, len(s)): 
                if(i == j):
                    pal[i][j] = True
                elif(i+1 == j): 
                    pal[i][j] = (s[i]==s[j])
                else: 
                    pal[i][j] = (s[i]==s[j] and pal[i+1][j-1]) 

        def dfs(s, s_i, e_i, curr_res):
            if e_i == len(s): 
                if s_i == len(s):
                    res.append(curr_res[:])
            else: 
                if pal[s_i][e_i]:
                    curr_res.append(s[s_i:e_i+1])
                    dfs(s, e_i+1, e_i+1, curr_res)
                    curr_res.pop()
                dfs(s, s_i, e_i+1, curr_res) 
        curr_res = []
        dfs(s, 0, 0, curr_res)

        return res