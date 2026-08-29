class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        visited = [False for _ in range(len(nums))]
        def dfs(res, sub_res):
            if len(sub_res) == len(nums):
                res.append(sub_res[:])
            else:
                i=0
                while i<len(nums):
                    if not visited[i]:
                        visited[i] = True
                        sub_res.append(nums[i])
                        dfs(res, sub_res)
                        visited[i] = False
                        sub_res.pop()
                        i += 1
                        while i<len(nums) and nums[i] == nums[i-1]:
                            i += 1
                    else:
                        i += 1
        dfs(res, [])
        return res