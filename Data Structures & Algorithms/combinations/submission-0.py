class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(index, res, sub_res):
            if index == n+1:
                if len(sub_res)==k:
                    res.append(sub_res[:])
            else:
                if len(sub_res) < k:
                    sub_res.append(index)
                    dfs(index+1, res, sub_res)
                    sub_res.pop()
                dfs(index+1, res, sub_res)
        dfs(1, res, [])
        return res