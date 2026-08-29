import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        insert_index = bisect.bisect_left(nums, target)
        if insert_index<len(nums) and nums[insert_index] == target:
            return insert_index
        return -1