class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        prev_odd_cnt, prev_even_cnt = 0, 1
        curr_sum = 0

        res = 0

        for num in arr:
            curr_sum += num

            if curr_sum%2:
                res += prev_even_cnt
            else:
                res += prev_odd_cnt
            
            
            if curr_sum%2:
                prev_odd_cnt += 1
            else:
                prev_even_cnt += 1

        return res

        