class Solution:
    def overlapping(self, interval1, interval2): 
        return not (interval1[0]>interval2[1] or interval1[1]<interval2[0])

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        non_overlapping_intervals = []
        for i in range(len(intervals)-1): 
            if self.overlapping(intervals[i], intervals[i+1]): 
                intervals[i+1][0] = intervals[i][0]
                intervals[i+1][1] = max(intervals[i][1], intervals[i+1][1])
            else: 
                non_overlapping_intervals.append(intervals[i])
        non_overlapping_intervals.append(intervals[len(intervals)-1])
        return non_overlapping_intervals