class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        prev_count = [[0 for j in range(n+1)] for i in range(m+1)]

        for i in range(len(strs)):
            zero_count = strs[i].count("0")
            one_count = len(strs[i]) - zero_count
            
            for p in range(m-zero_count, -1, -1):
                for q in range(n-one_count, -1, -1):
                    prev_count[p+zero_count][q+one_count]  = max(
                        prev_count[p+zero_count][q+one_count],
                        prev_count[p][q]+1
                    )
            
        res = 0

        for i in range(m+1):
            for j in range(n+1):
                res = max(res, prev_count[i][j])


        return res