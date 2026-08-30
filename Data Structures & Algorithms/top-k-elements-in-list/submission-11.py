import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        # Returns the k largest keys based on their values in the dictionary
        return heapq.nlargest(k, count.keys(), key=count.get)