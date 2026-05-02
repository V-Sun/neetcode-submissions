"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key = lambda i: i.start)
        rooms = 0

        while intervals:
            rooms += 1
            res = []
            curEnd = intervals[0].end
            for i in range(1, len(intervals)):
                curRoom = intervals[i]
                if curEnd > curRoom.start:
                    res.append(intervals[i])
                else:
                    curEnd = curRoom.end
            intervals = res
        
        return rooms
