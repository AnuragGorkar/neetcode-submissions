class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range((n+1)//2):
            for j in range(i, n-i-1):
                p, q = i, j
                temp = matrix[p][q]
                for _ in range(4):
                    p, q = q, n-p-1
                    print(p, q)
                    matrix[p][q], temp = temp, matrix[p][q]    
