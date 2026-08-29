class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        nums.sort()
        
        i, j = 0, 1
        curr_length, max_length = 1, 1
        while j<len(nums):
            if nums[j] == nums[i]:
                j += 1  
            elif nums[j] == (nums[i]+1):
                i = j
                curr_length += 1
                j += 1
            else:
                max_length = max(curr_length, max_length)
                curr_length = 1
                i = j
                j+=1
        return max(curr_length, max_length)