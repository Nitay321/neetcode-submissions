class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        i = 0
        res = []

        if newInterval[1] < intervals[0][0]:
            res.append(newInterval)
            while i < len(intervals):
                res.append(intervals[i])
                i += 1
            return res


        

        while i < len(intervals):
            if i+1 < len(intervals) and intervals[i][1] < newInterval[0] and newInterval[1] < intervals[i+1][0]:
                res.append(intervals[i])
                res.append(newInterval)
                i += 1
                while i < len(intervals):
                    res.append(intervals[i]) 
                    i += 1
                return res 

            if intervals[i][1] >= newInterval[0]:
                res.append([min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])])
                break
            else:
                res.append(intervals[i])  

            i += 1

        if i == len(intervals):
            res.append(newInterval)
            return res
        
        while i < len(intervals):
            if intervals[i][0] <= newInterval[1]:
                res[len(res)-1][1] = max(intervals[i][1], newInterval[1]) 
            else:
                res.append(intervals[i])       
            i += 1
        
        return res
        
            
            
     