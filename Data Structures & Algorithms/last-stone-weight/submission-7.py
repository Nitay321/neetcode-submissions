import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        
        while len(max_heap) > 1:
            y = -max_heap[0]
            x = -max_heap[1] if len(max_heap) == 2 or -max_heap[1] > -max_heap[2] else -max_heap[2]

            if y == x:
                heapq.heappop(max_heap)
                heapq.heappop(max_heap)
            else:
                z = y - x
                heapq.heappop(max_heap)
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, -z)
               
        if max_heap:
            return -max_heap[0]

        return 0  





  