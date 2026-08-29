class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        overall_diff = 0
        diff_array = [0] * len(gas)

        for i in range(len(gas)):
            diff_array[i] = gas[i]-cost[i]
            overall_diff += diff_array[i]

        if overall_diff<0:
            return -1
        else:
            start_index, pre_pos_value= -1, -1
            for i in range(len(diff_array)):
                if diff_array[i]>=0:
                    if start_index == -1 or pre_pos_value<0:
                        start_index = i
                    pre_pos_value = diff_array[i]
                else:
                    pre_pos_value += diff_array[i]

            return start_index           