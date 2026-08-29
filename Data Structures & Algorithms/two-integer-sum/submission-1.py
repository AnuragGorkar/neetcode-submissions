class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [[num, index] for index, num in enumerate(nums)]
        nums.sort()
        i, j = 0, len(nums)-1
        while i<j:
            if nums[i][0] + nums[j][0] == target:
                break
            elif nums[i][0] + nums[j][0] < target:
                i+=1
            else: 
                j-=1 
        return sorted([nums[i][1], nums[j][1]])
        