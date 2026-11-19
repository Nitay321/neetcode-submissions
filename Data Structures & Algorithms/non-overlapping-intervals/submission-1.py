import math
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        curr = [-math.inf,-math.inf]
        count = 0
        for interval in intervals:
            if interval[0] < curr[1]:
                count += 1
            else:
                curr = interval
        
        return count
       
        