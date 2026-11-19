"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda inter: inter.start)

        curr = Interval(math.inf,math.inf)
        for i in range(len(intervals)-1,-1,-1):
            if intervals[i].end <= curr.start:
                curr = intervals[i]
            else:
                return False
            
        
        return True



