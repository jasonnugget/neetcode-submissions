"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        newIntervals = []
        for interval in intervals:
            newIntervals.append([interval.start, interval.end])

        newIntervals = sorted(newIntervals)
        stack = []

        for i in range(len(newIntervals) - 1):
            if not stack:
                temp = newIntervals[i]

            else:
                temp = stack.pop()

            compare = newIntervals[i + 1]
            
            if temp[1] <= compare[0]:
                stack.append(temp)
                stack.append(compare)

            elif temp[0] >= compare[1]:
                stack.append(temp)
                stack.append(compare)

            else:
                return False

        return True