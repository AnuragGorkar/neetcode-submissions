class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col_mask, backward_diag_mask, forward_diag_mask = 0, 0, 0
        res = []

        def dfs(row, sub_res):
            nonlocal col_mask, backward_diag_mask, forward_diag_mask
            if row == n:
                res.append(sub_res[:])
            else:
                for col in range(n):
                    if not ((col_mask>>(n-col) & 1) or (forward_diag_mask>>(row+col) & 1) or (backward_diag_mask>>(n+row-col) & 1)):
                        sub_res_string = "."*col + "Q" + "."*(n-1-col)
                        sub_res.append(sub_res_string)
                        col_mask |= (1<<(n-col))
                        forward_diag_mask |= (1<<(row+col))
                        backward_diag_mask |= (1<<(n+row-col))

                        dfs(row+1, sub_res)

                        sub_res.pop()
                        col_mask ^= (1<<(n-col))
                        forward_diag_mask ^= (1<<(row+col))
                        backward_diag_mask ^= (1<<(n+row-col))

        dfs(0, [])
        return res