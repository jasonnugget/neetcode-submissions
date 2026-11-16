class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            prev = res.pop()
            if prev[1] < intervals[i][0]:
                res.append(prev)
                res.append(intervals[i])

            else:
                prev[0] = min(prev[0], intervals[i][0])
                prev[1] = max(prev[1], intervals[i][1])
                res.append(prev)

        return res