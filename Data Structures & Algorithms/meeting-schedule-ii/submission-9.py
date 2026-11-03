"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms = []
        intervals.sort(key=lambda x: x.start)

        for interval in intervals:
            if not rooms:
                heapq.heappush(rooms, interval.end)
                continue
            
            if rooms[0] > interval.start:
                heapq.heappush(rooms, interval.end)

            else:
                heapq.heappop(rooms)
                heapq.heappush(rooms, interval.end)

        return len(rooms)
                