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

        for i in range(len(s)): 
            for j in range(len(s)): 
                pal[i][j] = self.isPalindrome(s, i, j)

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