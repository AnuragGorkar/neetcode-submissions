class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[1], x[0]))
        print(intervals)
        removeCount = 0
        for i in range(len(intervals)-1):
            # overlapping
            if not (intervals[i][1] <= intervals[i+1][0] or intervals[i+1][1] <= intervals[i][0]):
                removeCount+=1
                intervals[i+1] = intervals[i]
        return removeCount
        