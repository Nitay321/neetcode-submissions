class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = [None]
        intervals.sort()
        prev = intervals[0]

        for interval in intervals:
            if interval[0] <= prev[1]:
                prev[0] = min(interval[0], prev[0])
                prev[1] = max(interval[1], prev[1])
                res[len(res)-1] = [prev[0], prev[1]]       
            else:
                res.append(interval)
                prev = interval
        
        return res


        