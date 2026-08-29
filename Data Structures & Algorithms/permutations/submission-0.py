class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        visited = [False for _ in range(n)]
        res = []
        def dfs(nums, visited, curr_res):
            if len(curr_res)==n: 
                res.append(curr_res[:])
            else: 
                for i in range(n):
                    if not visited[i]: 
                        visited[i] = True
                        curr_res.append(nums[i])
                        dfs(nums, visited, curr_res)
                        visited[i] = False
                        curr_res.pop() 
        dfs(nums, visited, [])
        return res        