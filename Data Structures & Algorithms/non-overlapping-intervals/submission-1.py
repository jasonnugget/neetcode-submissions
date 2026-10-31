class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = intervals[0][1]
        res = 0
        
        for i in range(1, len(intervals)):
            if prev > intervals[i][0]:
                res += 1
                prev = min(intervals[i][1], prev)

            else:
                prev = intervals[i][1]

        return res