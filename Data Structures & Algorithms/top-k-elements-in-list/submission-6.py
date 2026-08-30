from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums).most_common(k)
        result = []
        for element in counter:
            result.append(element[0])
        return result