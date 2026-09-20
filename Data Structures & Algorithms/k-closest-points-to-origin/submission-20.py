import math
import heapq
from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = set([])
        Id = defaultdict(list)
        for point in points:
            dist = point[0]*point[0] + point[1]*point[1]
            distances.add(dist)
            Id[dist].append(point)

        distances = list(distances)
        heapq.heapify(distances)
        res = []
        while k > 0:
            dist = heapq.heappop(distances)
            while Id[dist] and k>0:
                point = Id[dist].pop()
                res.append(point)
                k -= 1
                
        return res
          
        