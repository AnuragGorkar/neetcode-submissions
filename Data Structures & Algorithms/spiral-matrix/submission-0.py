class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        r_lim, d_lim, l_lim, u_lim = 0, 0, 0, 1

        res = []
        i, j = 0, 0
        while len(res)<(m*n):
            while j<(m-r_lim):
                res.append(matrix[i][j])
                j+=1
            j-=1
            i+=1
            r_lim += 1
            while i<(n-d_lim):
                res.append(matrix[i][j])
                i+=1
            i-=1
            j-=1
            d_lim += 1
            while j>=(0+l_lim):
                res.append(matrix[i][j])
                j-=1
            j+=1
            i-=1
            l_lim += 1
            while i>=(0+u_lim):
                res.append(matrix[i][j])
                i-=1
            i+=1
            j+=1
            u_lim += 1

            
        return res[0:m*n]