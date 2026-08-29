"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from sortedcontainers import SortedDict

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        line_sweep_dict = SortedDict()

        for interval in intervals: 
            if interval.start not in line_sweep_dict: 
                line_sweep_dict[interval.start] = 1
            else: 
                line_sweep_dict[interval.start] += 1

            if interval.end not in line_sweep_dict: 
                line_sweep_dict[interval.end] = -1
            else: 
                line_sweep_dict[interval.end] -= 1

        overlapCount = 0
        for val in line_sweep_dict.values(): 
            overlapCount += val
            if overlapCount>1: 
                return False
            
        return True





            
