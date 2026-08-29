class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_count = 0
        zero_index = -1
        for index, num in enumerate(nums):
            if num == 0:
                zero_count += 1
                zero_index = index
                if zero_count>1:
                    return [0] * len(nums)
            else:
                total_product = total_product * num
        if zero_count == 1:
            res = [0] * len(nums)
            res[zero_index] = total_product
            return res
        else:
            res = [total_product] * len(nums)
            for index, num in enumerate(nums):
                res[index] //= num
            return res