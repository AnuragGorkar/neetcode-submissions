class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        def dfs(v_low, v_high, h_low, h_high):
            if v_low>v_high or h_low>h_high: 
                return False
            v_mid = (v_low + v_high)//2
            h_mid = (h_low + h_high)//2
            if(matrix[v_mid][h_mid] == target): 
                return True
            else: 
                if(target<matrix[v_mid][h_mid]):
                    return dfs(v_low, v_mid, h_low, h_mid-1) or dfs(v_low, v_mid-1, h_mid, h_high)
                else: 
                    return dfs(v_mid+1, v_high, h_low, h_mid) or dfs(v_mid, v_high, h_mid+1, h_high)
        
        return dfs(0, m-1, 0, n-1)


        