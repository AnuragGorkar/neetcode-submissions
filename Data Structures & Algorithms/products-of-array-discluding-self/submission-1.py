class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        
        current_product = nums[0]
        for i in range(1, len(nums)):
            res[i] = current_product
            current_product *= nums[i]
        
        current_product = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            res[i] = current_product*res[i]
            current_product *= nums[i]
            
        return res