class Solution:
    def getCountLessThan(self, nums, val):
        low, high = 0, len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if val<nums[mid]:
                high = mid-1
            else: 
                low = mid+1
        low_max = low

        low, high = 0, len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if val<=nums[mid]:
                high = mid-1
            else: 
                low = mid+1
        return low, low_max

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        lt_target = (m+n-1)//2

        # Search in nums1
        low, high = 0, len(nums1)-1
        while low<=high:
            mid = (low+high)//2

            lt_nums1 = mid
            lt_nums2_min, lt_nums2_max = self.getCountLessThan(nums2, nums1[mid])

            lt_total_min = lt_nums1 + lt_nums2_min
            lt_total_max = lt_nums1 + lt_nums2_max 
            print(nums1[lt_nums1], mid, lt_nums2_min, lt_nums2_max, lt_total_min, lt_total_max)
            if lt_target<=lt_total_max and lt_target>=lt_total_min:
                if (m+n)%2:
                    return nums1[mid]
                else:
                    if lt_target == lt_total_max:
                        lt_nums2_min = lt_nums2_max
                    next_num = min(
                        # In nums1
                        nums1[mid+1] if (mid+1) < len(nums1) else 1e9,
                        # In nums2
                        nums2[lt_nums2_min] if lt_nums2_min < len(nums2) else 1e9 
                    )
                    return (nums1[mid] + next_num)/2
            elif lt_total_max > lt_target:
                high = mid-1
            else:
                low = mid+1

        print("-----------------")
        # Search in nums2
        low, high = 0, len(nums2)-1
        while low<=high:
            mid = (low+high)//2

            lt_nums2 = mid
            lt_nums1_min, lt_nums1_max = self.getCountLessThan(nums1, nums2[mid])

            lt_total_min = lt_nums1_min + lt_nums2 
            lt_total_max = lt_nums1_max + lt_nums2  

            print(nums2[lt_nums2], mid, lt_nums1_min, lt_nums1_max, lt_total_min, lt_total_max)
            if lt_target<=lt_total_max and lt_target>=lt_total_min:
                if (m+n)%2:
                    return nums2[mid]
                else:
                    if lt_target == lt_total_max:
                        lt_nums1_min = lt_nums1_max
                    next_num = min(
                        # In nums2
                        nums2[mid+1] if (mid+1) < len(nums2) else 1e9,
                        # In nums1
                        nums1[lt_nums1_min] if lt_nums1_min < len(nums1) else 1e9 
                    )
                    return (nums2[mid] + next_num)/2
            elif lt_total_max > lt_target:
                high = mid-1
            else:
                low = mid+1
        
        return 0.0