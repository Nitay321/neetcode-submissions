import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            dis = x**2 + y**2
            heap.append([dis,[x,y]])
        
        heapq.heapify(heap)

        res = []
        while k>0:
            dis, point = heapq.heappop(heap)
            res.append(point)
            k-=1
        return res
        
        

        





        