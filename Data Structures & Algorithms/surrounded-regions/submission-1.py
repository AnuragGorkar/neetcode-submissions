class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        di_dj = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(i, j): 
            for di, dj in di_dj: 
                ni, nj = i+di, j+dj
                if ni>=0 and nj>=0 and ni<m and nj<n and board[ni][nj] == 'O':
                    board[ni][nj] = '-'
                    dfs(ni, nj)

        j = 0
        for i in range(m):
            if board[i][j] == 'O': 
                board[i][j] = '-'
                dfs(i, j)

        j = n-1
        for i in range(m):
            if board[i][j] == 'O': 
                board[i][j] = '-'
                dfs(i, j)

        i = 0
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = '-' 
                dfs(i, j)

        i = m-1
        for j in range(n):
            if board[i][j] == 'O': 
                board[i][j] = '-'
                dfs(i, j)

        for i in range(m):
            for j in range(n): 
                if board[i][j] == '-':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'