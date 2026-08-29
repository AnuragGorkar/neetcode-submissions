class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]
        
        def dfs(i, j, index):
            if index == len(word): 
                return True
            elif i<0 or j<0 or i>= m or j>=n or visited[i][j] or board[i][j] != word[index]: 
                return False
            else:
                visited[i][j] = True
                ret_val = dfs(i+1, j, index+1) or dfs(i-1, j, index+1) or dfs(i, j+1, index+1) or dfs(i, j-1, index+1) 
                visited[i][j] = False
                return ret_val
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False
        