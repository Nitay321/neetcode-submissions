import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.k_largest_nums = nums
        heapq.heapify(self.k_largest_nums)

        while len(self.k_largest_nums) > k:
             heapq.heappop(self.k_largest_nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.k_largest_nums, val)

        if len(self.k_largest_nums) > self.k:
            heapq.heappop(self.k_largest_nums)
        
        return self.k_largest_nums[0]
        

        

        
