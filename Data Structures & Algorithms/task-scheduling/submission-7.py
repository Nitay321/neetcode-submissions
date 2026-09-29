from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
    
        heap = [0]*26
        for task in tasks:
            index = ord(task) - ord("A")
            heap[index] += 1

        max_heap = [-task for task in heap if task != 0]
        heapq.heapify(max_heap)

        time = 0
        queue = collections.deque([])

        while max_heap or queue:
            time += 1
            if queue and queue[0][0] <= time:
                first = queue.popleft()
                heapq.heappush(max_heap, first[1])
            if max_heap:
                element = heapq.heappop(max_heap)
                if element < -1:
                    queue.append((time + n + 1, element + 1))

        
        return time

        

        