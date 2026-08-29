class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        box_set = defaultdict(set)

        for i in range(m):
            for j in range(n):
                current_char = board[i][j]
                if current_char == '.':
                    continue
                
                if current_char in row_set[i]:
                    return False
                row_set[i].add(current_char)

                if current_char in col_set[j]:
                    return False
                col_set[j].add(current_char)

                if current_char in box_set[(i//3)*3+(j//3)]:
                    return False
                box_set[(i//3)*3+(j//3)].add(current_char)
        
        return True
        