class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reached = nums[0]
        for i in range(1, len(nums)):
            if i>max_reached:
                break
            max_reached = max(max_reached, i + nums[i])
            if max_reached >= (len(nums)-1):
                break
        return max_reached >= (len(nums)-1)