import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while max_heap and len(max_heap) > 1:
            y = -heapq.heappop(max_heap)
            x = -heapq.heappop(max_heap)

            if y > x:
               heapq.heappush(max_heap,x-y)
            
        if max_heap:
            return -max_heap[0]
        return 0
 


        
        