class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        tot_sum = sum(nums)
        tot_rem = tot_sum % p

        if tot_rem == 0:
            return 0

        curr_sum = 0
        prev_mods = {0: 0}

        res = len(nums)

        for i in range(len(nums)):
            curr_sum += nums[i]
            curr_rem = curr_sum % p

            req_rem = (curr_rem - tot_rem) % p

            if req_rem in prev_mods:
                res = min(res, i + 1 - prev_mods[req_rem])

            prev_mods[curr_rem] = i + 1

        return res if res < len(nums) else -1
