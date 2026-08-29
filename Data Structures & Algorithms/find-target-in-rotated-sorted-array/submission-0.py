class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findPivot(nums):
            low, high = 0, len(nums) - 1
            while low < high:
                mid = (low + high) // 2
                if nums[mid] > nums[high]:
                    low = mid + 1
                else:
                    high = mid
            return low  # index of smallest element
        
        n = len(nums)
        pivot = findPivot(nums)
        
        # Normal binary search with adjusted indices
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            realMid = (mid + pivot) % n   # rotate index back
            if nums[realMid] == target:
                return realMid
            elif nums[realMid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
        