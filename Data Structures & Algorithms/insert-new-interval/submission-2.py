class Solution:
    def overlapping(self, interval1, interval2): 
        if not interval1 or not interval2: 
            return False
        else: 
            return not (interval1[1]<interval2[0] or interval1[0]>interval2[1])

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = []
        for interval in intervals: 
            if not self.overlapping(interval, newInterval): 
                if newInterval and interval[0] > newInterval[1]: 
                    new_intervals.append(newInterval)
                    newInterval = None
                new_intervals.append(interval)
            elif newInterval:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        if newInterval: 
            new_intervals.append(newInterval)
        return new_intervals
        