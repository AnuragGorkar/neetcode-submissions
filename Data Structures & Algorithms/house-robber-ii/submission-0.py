class Solution:
    def rob1(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1: 
            return nums[0]
        nums[1] = max(nums[0], nums[1])
        for i in range(2, n): 
            nums[i] = max(nums[i-2]+nums[i], nums[i-1])
        return nums[n-1]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1: 
            return nums[0]
        return max(self.rob1(nums[1:]), self.rob1(nums[:n-1]))
        
        
        