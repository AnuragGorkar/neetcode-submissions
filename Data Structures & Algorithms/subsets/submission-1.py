class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        mask = 0
        res= []
        for i in range(pow(2, len(nums))): 
            sub_res = []
            for j in range(len(nums)): 
                to_take_or_not_take = (mask >> j) & 1
                if to_take_or_not_take:
                    sub_res.append(nums[j])
            res.append(sub_res[:])
            mask+=1
        return res


            

        